from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from bot.config import START_PIC

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [[InlineKeyboardButton("Join Channel", url="https://t.me/+Us68QoIPUN8zNjU1")]]
    reply_markup = InlineKeyboardMarkup(buttons)

    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=START_PIC,
        caption=f"👋 Hello {update.effective_user.first_name}, welcome to the Auto-Approve Bot!",
        reply_markup=reply_markup
    )
