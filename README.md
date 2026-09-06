# 🤖 AI Lead Capture Widget

An AI-powered, intelligent lead capture chat widget built with **FastAPI**, **Google Gemini API**, and **SQLite**. Designed for portfolio and service websites to engage visitors, answer queries in real-time, and automatically extract contact details into a structured database.

---

## ✨ Key Features

- **🤖 AI Support Assistant**: Powered by Google Gemini (`gemini-2.5-flash`) for fast, natural customer support responses.
- **📧 Automated Lead Extraction**: Regex filter auto-detects user email addresses from chat messages.
- **💾 Database Persistence**: Permanently stores captured leads (email, initial message, timestamp) in a local SQLite database (`leads.db`).
- **⚡ High-Performance REST API**: Built with FastAPI, including async support and automated Swagger UI documentation.
- **🎨 Easy Integration**: Minimal HTML/JS chat widget ready to be embedded into any website or portfolio.

---

## 🛠️ Tech Stack

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/) + [Uvicorn](https://www.uvicorn.org/)
- **Database / ORM**: [SQLite](https://www.sqlite.org/) + [SQLAlchemy](https://www.sqlalchemy.org/)
- **AI Model**: [Google Gemini API](https://ai.google.dev/) (`google-generativeai`)
- **Frontend**: HTML5 / CSS3 / Vanilla JavaScript

---

## 📁 Project Structure

```text
ai-lead-widget/
├── backend/
│   ├── main.py          # FastAPI endpoints, Gemini API, and regex extraction logic
│   ├── database.py      # SQLAlchemy models and database connection setup
│   ├── leads.db         # SQLite database file (auto-created on startup)
│   └── .env             # Environment file storing secret API keys
└── widget.html          # Chat widget frontend interface
