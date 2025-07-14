# Optional: for future custom welcome messages
async def send_welcome_message(context, chat_id, user_id):
    await context.bot.send_message(
        chat_id=chat_id,
        text=f"Welcome, <a href='tg://user?id={user_id}'>new member</a>!",
        parse_mode="HTML"
    )
