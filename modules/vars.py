import os

API_ID    = os.environ.get("API_ID", "26513107")
API_HASH  = os.environ.get("API_HASH", "f14ce4b58dc8812cfc9665588472f2d4")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7550260070:AAFolY9g88nS46pRve3TG6J92PNGrVKTvcY") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
