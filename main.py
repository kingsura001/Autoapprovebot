from telegram.ext import CommandHandler, ChatJoinRequestHandler
from bot.start import build_application, start_bot
from bot.handlers.commands_handler import start_command
from bot.handlers.join_request_handler import join_request

def main():
    app = build_application()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(ChatJoinRequestHandler(join_request))

    start_bot(app)

if __name__ == "__main__":
    main()
