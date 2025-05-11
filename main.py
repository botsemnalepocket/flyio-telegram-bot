
import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_ID")

def start(update: Update, context: CallbackContext) -> None:
    if str(update.effective_chat.id) == CHAT_ID:
        context.bot.send_message(chat_id=update.effective_chat.id, text="✅ Botul este activ!")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="⛔ Acces interzis.")

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.start_polling()
updater.idle()
