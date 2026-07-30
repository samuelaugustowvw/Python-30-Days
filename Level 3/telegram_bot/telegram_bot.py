import os
import logging
from telegram import Update
from telegram.ext import(
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
async def start(update:Update,context:ContextTypes.DEFAULT_TYPE):
    name = update.effective_user.first_name
    await update.message.reply_text(
        f"Hi {name}!\nType /help to see what I can do."
    )
async def help_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Here's what I can do:\n"
        "/start - say hello\n"
        "/help - show this message\n"
        "/echo <text> - repeat your text"
    )
async def echo(update:Update,context:ContextTypes.DEFAULT_TYPE):
    if context.args:
        text = " ".join(context.args)
        await update.message.reply_text(text)
    else:
        await update.message.reply_text("Usage: /echo <text>")
async def handle_message(update:Update,context:ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    await update.message.reply_text(f'You said: "{user_text}"')
def main():
    if not TOKEN:
        print("No token found.")
        print("Set it with:  export TELEGRAM_BOT_TOKEN=your_token_here")
        return
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start",start))
    app.add_handler(CommandHandler("help",help_command))
    app.add_handler(CommandHandler("echo",echo))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,handle_message))
    print("Bot is running... Press Ctrl+C to stop.")
    app.run_polling()
if __name__ == "__main__":
    main()