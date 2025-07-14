import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
LOG_CHANNEL_ID = int(os.getenv("LOG_CHANNEL_ID"))
AUTO_APPROVE_ENABLED = os.getenv("AUTO_APPROVE_ENABLED", "true").lower() == "true"
START_PIC = os.getenv("START_PIC", "https://your-default-image-link.com/start.jpg")
