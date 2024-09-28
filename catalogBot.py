import asyncio
import random
import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import nest_asyncio
import os

token = os.getenv('TELEGRAM_TOKEN')

# Allow nested event loops
nest_asyncio.apply()

# Replace with your web app URL
WEB_APP_URL = "https://at0mskxiv.github.io/testCatalog/index.html"  # Update with the correct URL of your Mini App

# Start command to introduce the bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Магазин МИМИЛАПКИ", web_app=dict(url=WEB_APP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Магазин МИМИЛАПКИ приветствует вас!\n Нажмите на кнопку ниже чтобы открыть миниприложение.', reply_markup=reply_markup)

async def main() -> None:
    application = ApplicationBuilder().token(token).build()

    # Register commands
    application.add_handler(CommandHandler('start', start))

    # Start polling and run the bot
    await application.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
