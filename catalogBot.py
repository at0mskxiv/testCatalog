import asyncio
from datetime import datetime, timedelta
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import nest_asyncio

# Get the Telegram token from environment variables
token = os.getenv('TELEGRAM_TOKEN')

# Allow nested event loops
nest_asyncio.apply()

# Replace with your web app URL
WEB_APP_URL = "https://at0mskxiv.github.io/testCatalog/index.html"  # Update with the correct URL of your Mini App

# Cooldown variable
last_start_time = None
COOLDOWN_DURATION = timedelta(seconds=5)  # 5 seconds cooldown

# Start command to introduce the bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global last_start_time
    now = datetime.now()

    # Check if cooldown period has passed
    if last_start_time and now - last_start_time < COOLDOWN_DURATION:
        return  # Ignore the command if it's within cooldown

    last_start_time = now  # Update last start time

    keyboard = [
        [InlineKeyboardButton("Магазин МИМИЛАПКИ", web_app=dict(url=WEB_APP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send a welcome message with the button
    await update.message.reply_text('Магазин МИМИЛАПКИ приветствует вас!\n Нажмите на кнопку ниже чтобы открыть миниприложение.', reply_markup=reply_markup)

async def main() -> None:
    application = ApplicationBuilder().token(token).build()

    # Register commands
    application.add_handler(CommandHandler('start', start))

    # Start polling and run the bot
    await application.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
