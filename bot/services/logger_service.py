from bot.config import LOG_CHANNEL_ID

async def log_approval(context, update):
    user = update.effective_user
    await context.bot.send_message(
        chat_id=LOG_CHANNEL_ID,
        text=f"✅ Approved {user.first_name} (`{user.id}`) to join `{update.effective_chat.title}`",
        parse_mode="Markdown"
    )
