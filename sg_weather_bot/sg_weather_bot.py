from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler, CallbackContext
from dotenv import load_dotenv
import os
from pathlib import Path

## to call data from env
main_path = Path(__file__).parent.parent
dotenv_path = main_path / '.env'
# Load the environment variables from the specified .env file
load_dotenv(dotenv_path)

# telegram bot details
BOT_TOKEN = os.getenv('BOT_TOKEN')
BOT_USERNAME = os.getenv('BOT_USERNAME')


# Commands
## /start what the bot says when a user starts the bot
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Welcome to the Singapore Weather Bot~ Here, you can easily find out the weather condition around SG!')

## /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Click start to get started!')

## /weather_forecast
async def weather_forecast(update: Update, context: CallbackContext):
    # create buttons
    buttons = [
        [InlineKeyboardButton("AMK", callback_data='AMK')],
        [InlineKeyboardButton("Bukit Timah", callback_data='Bukit Timah')],
    ]
    reply_buttons = InlineKeyboardMarkup(buttons)
    await update.message.reply_text('Hello! Choose your area of interest~', reply_markup = reply_buttons)

## /rainfall_now
async def rainfall_now(update: Update, context: CallbackContext):
    # create buttons
    buttons = [
        [InlineKeyboardButton("AMK", callback_data='AMK')],
        [InlineKeyboardButton("Serangoon", callback_data='Serangoon')],
    ]
    reply_buttons = InlineKeyboardMarkup(buttons)
    await update.message.reply_text('Hello! Choose your area of interest~', reply_markup = reply_buttons)

# Responses
def handle_response(text: str) -> str:
    return


# responding user
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # this code will tell you whether is it a group chat or not
    message_type: str = update.message.chat.type 
    # incoming text from user
    text:str = update.message.text
    
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text:str = text.replace(BOT_USERNAME, '').strip()
            response:str = handle_response(new_text)
        else:
            return
    else:
        ## private chat response
        response:str = handle_response(text)   

    await update.message.reply_text(response)     

async def handle_buttons(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer() #ack the button press

    # handle the data based on callback data tag
    if query.data == 'AMK':
        await query.edit_message_text(text="You have chosen AMK!")
    elif query.data == 'Serangoon':
        await query.edit_message_text(text="You have chosen Serangoon!")
    elif query.data == 'Bukit Timah':
        await query.edit_message_text(text="You have chosen Bukit Timah!")


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == "__main__":
    print("Starting bot")
    app = Application.builder().token(BOT_TOKEN).build()

    # commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('weather_forecast', weather_forecast))
    app.add_handler(CommandHandler('rainfall_now', rainfall_now))


    # waiting for messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_handler(CallbackQueryHandler(handle_buttons))

    # errors
    app.add_error_handler(error)

    # polling
    # checks every 5s for user response
    print("Polling")
    app.run_polling(poll_interval = 3)