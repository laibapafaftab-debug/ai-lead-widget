import os
import re
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import google.generativeai as genai

from database import SessionLocal, Lead, init_db

load_dotenv()

# Gemini Setup
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

app = FastAPI(title="AI Lead Widget API")
init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class ChatRequest(BaseModel):
    message: str

@app.post("/api/chat")
def chat_endpoint(request: ChatRequest, db: Session = Depends(get_db)):
    user_message = request.message
    
    # Email Regex Extraction
    email_match = re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', user_message)
    captured_lead = False
    
    if email_match:
        extracted_email = email_match.group(0)
        existing_lead = db.query(Lead).filter(Lead.email == extracted_email).first()
        if not existing_lead:
            new_lead = Lead(email=extracted_email, message=user_message)
            db.add(new_lead)
            db.commit()
            captured_lead = True

    try:
        # Gemini AI Response
        response = model.generate_content(
            f"You are a helpful customer support assistant for a services website. Answer concisely: {user_message}"
        )
        ai_reply = response.text
        if captured_lead:
            ai_reply += "\n\n(Shukriya! Aap ka email save kar liya gaya hai.)"
            
        return {"reply": ai_reply, "captured_lead": captured_lead}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Gemini API Error: {str(e)}")

@app.get("/api/leads")
def get_leads(db: Session = Depends(get_db)):
    leads = db.query(Lead).all()
    return leads
