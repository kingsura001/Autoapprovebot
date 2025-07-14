import os
from dotenv import load_dotenv

# Load .env file in local development (not necessary on Render, but safe)
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
LOG_CHANNEL_ID = os.getenv("LOG_CHANNEL_ID")
START_PIC = os.getenv("START_PIC")
AUTO_APPROVE_ENABLED = True  # or False, depending on your logic

# Convert ADMIN_IDS string to list of integers
admin_ids_str = os.getenv("ADMIN_IDS", "")
if admin_ids_str:
    ADMIN_IDS = list(map(int, admin_ids_str.split()))
else:
    ADMIN_IDS = []
