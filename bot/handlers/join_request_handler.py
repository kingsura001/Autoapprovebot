from telegram import Update
from telegram.ext import ContextTypes
from bot.config import AUTO_APPROVE_ENABLED, LOG_CHANNEL_ID
from bot.services.logger_service import log_approval

async def join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if AUTO_APPROVE_ENABLED:
        await context.bot.approve_chat_join_request(
            chat_id=update.effective_chat.id,
            user_id=update.effective_user.id
        )
        await log_approval(context, update)
