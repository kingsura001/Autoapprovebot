from telegram.ext import ApplicationBuilder
from bot.config import BOT_TOKEN

def start_bot(application):
    application.run_polling()

def build_application():
    return ApplicationBuilder().token(BOT_TOKEN).build()
