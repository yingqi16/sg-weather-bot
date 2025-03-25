from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler, CallbackContext, ConversationHandler
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

# weather forecast conv
WF_FIRST_QUESTION, WF_SECOND_QUESTION = range(2)


# query api
def get_weather_details(area):
    return 'NA'


# Commands
## /start what the bot says when a user starts the bot
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Welcome to the Singapore Weather Bot~ Here, you can easily find out the weather condition around SG!')

## /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Click start to get started!')

# Function to cancel the conversation
def cancel(update, context):
    update.message.reply_text("Conversation cancelled.")
    return ConversationHandler.END

## /weather_forecast
async def get_weather_forecast_area_by_first_letter(update: Update, context: CallbackContext):
    buttons = [
        [InlineKeyboardButton("A-D", callback_data='A_D_weather_forecast')],
        [InlineKeyboardButton("E-J", callback_data='E_J_weather_forecast')],
        [InlineKeyboardButton("K-N", callback_data='K_N_weather_forecast')],
        [InlineKeyboardButton("O-R", callback_data='O_R_weather_forecast')],
        [InlineKeyboardButton("S-V", callback_data='S_V_weather_forecast')],
        [InlineKeyboardButton("W-Z", callback_data='W_Z_weather_forecast')]

    ]
    reply_buttons = InlineKeyboardMarkup(buttons)
    await update.message.reply_text("Hello! Which area's 2h weather forecast are you looking at?", reply_markup = reply_buttons)
    return WF_FIRST_QUESTION

async def weather_forecast(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer() #ack the button press

    # handle the data based on callback data tag
    # create buttons
    if query.data == 'A_D_weather_forecast':
        buttons = [
        [InlineKeyboardButton("Ang Mo Kio", callback_data='AMK_weather_forecast')],
        [InlineKeyboardButton("Bedok", callback_data='Bedok_weather_forecast')],
        [InlineKeyboardButton("Bishan", callback_data='Bishan_weather_forecast')],
        [InlineKeyboardButton("Boon Lay", callback_data='BL_weather_forecast')],
        [InlineKeyboardButton("Bukit Batok", callback_data='BB_weather_forecast')],
        [InlineKeyboardButton("Bukit Merah", callback_data='BM_weather_forecast')],
        [InlineKeyboardButton("Bukit Panjang", callback_data='BP_weather_forecast')],
        [InlineKeyboardButton("Bukit Timah", callback_data='BT_weather_forecast')],
        [InlineKeyboardButton("Central Water Catchment", callback_data='CWC_weather_forecast')],
        [InlineKeyboardButton("Changi", callback_data='Changi_weather_forecast')],
        [InlineKeyboardButton("Choa Chu Kang", callback_data='CCK_weather_forecast')],
        [InlineKeyboardButton("City", callback_data='City_weather_forecast')],
        [InlineKeyboardButton("Clementi", callback_data='Clementi_weather_forecast')]]
    elif query.data == 'E_J_weather_forecast':
        buttons = [
        [InlineKeyboardButton("Geylang", callback_data='Geylang_weather_forecast')],
        [InlineKeyboardButton("Hougang", callback_data='Hougang_weather_forecast')],
        [InlineKeyboardButton("Jalan Bahar", callback_data='JB_weather_forecast')],
        [InlineKeyboardButton("Jurong East", callback_data='JE_weather_forecast')],
        [InlineKeyboardButton("Jurong Island", callback_data='JI_weather_forecast')],
        [InlineKeyboardButton("Jurong West", callback_data='JW_weather_forecast')]]
    elif query.data == 'K_N_weather_forecast':
        buttons = [
            [InlineKeyboardButton("Kallang", callback_data='Kallang_weather_forecast')],
            [InlineKeyboardButton("Lim Chu Kang", callback_data='LCK_weather_forecast')],
            [InlineKeyboardButton("Mandai", callback_data='Mandai_weather_forecast')],
            [InlineKeyboardButton("Marine Parade", callback_data='MP_weather_forecast')],
            [InlineKeyboardButton("Novena", callback_data='Novena_weather_forecast')]
        ]
    elif query.data == 'O_R_weather_forecast':
        buttons = [
            [InlineKeyboardButton("Pasir Ris", callback_data='PR_weather_forecast')],
        [InlineKeyboardButton("Paya Lebar", callback_data='PL_weather_forecast')],
        [InlineKeyboardButton("Pioneer", callback_data='Pioneer_weather_forecast')],
        [InlineKeyboardButton("Pulau Tekong", callback_data='PT_weather_forecast')],
        [InlineKeyboardButton("Pulau Ubin", callback_data='PU_weather_forecast')],
        [InlineKeyboardButton("Punggol", callback_data='Punggol_weather_forecast')],
        [InlineKeyboardButton("Queenstown", callback_data='Queenstown_weather_forecast')]
        ]
    elif query.data == "S_V_weather_forecast":
        buttons = [
            [InlineKeyboardButton("Seletar", callback_data='Seletar_weather_forecast')],
        [InlineKeyboardButton("Sembawang", callback_data='Sembawang_weather_forecast')],
        [InlineKeyboardButton("Sengkang", callback_data='Sengkang_weather_forecast')],
        [InlineKeyboardButton("Sentosa", callback_data='Sentosa_weather_forecast')],
        [InlineKeyboardButton("Serangoon", callback_data='Serangoon_weather_forecast')],
        [InlineKeyboardButton("Southern Islands", callback_data='SI_weather_forecast')],
        [InlineKeyboardButton("Sungei Kadut", callback_data='SK_weather_forecast')],
        [InlineKeyboardButton("Tampines", callback_data='Tampines_weather_forecast')],
        [InlineKeyboardButton("Toa Payoh", callback_data='TP_weather_forecast')],
        [InlineKeyboardButton("Tuas", callback_data='Tuas_weather_forecast')]
        ]
    else :
        buttons = [
            [InlineKeyboardButton("Western Islands", callback_data='WI_weather_forecast')],
        [InlineKeyboardButton("Western Water Catchment", callback_data='WWC_weather_forecast')],
        [InlineKeyboardButton("Woodlands", callback_data='Woodlands_weather_forecast')],
        [InlineKeyboardButton("Yishun", callback_data='Yishun_weather_forecast')]
        ]
    reply_buttons = InlineKeyboardMarkup(buttons)
    # update.message.reply_text is used when you are handling a normal message. since this is a callback query, we should use update.callback_query
    # await update.message.reply_text("Hello! Which exact area's 2h weather forecast are you looking for?", reply_markup = reply_buttons)
    await query.edit_message_text("Select the exact area", reply_markup = reply_buttons)
    return WF_SECOND_QUESTION

async def get_weather_forecast_by_area(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer() #ack the button press
    response = query.data
    weather = get_weather_details(response)

    await query.message.reply_text(f"Hello! The weather at {response} is {weather}")
    return ConversationHandler.END

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

# async def handle_buttons(update: Update, context: CallbackContext):
#     query = update.callback_query
#     await query.answer() #ack the button press

#     # handle the data based on callback data tag
#     if query.data == 'get_weather_forecast_area_by_first_letter':
#         await weather_forecast()
#     elif query.data == 'Serangoon':
#         await query.edit_message_text(text="You have chosen Serangoon!")
#     elif query.data == 'Bukit Timah':
#         await query.edit_message_text(text="You have chosen Bukit Timah!")


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == "__main__":
    print("Starting bot")
    app = Application.builder().token(BOT_TOKEN).build()

    # commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    # app.add_handler(CommandHandler('weather_forecast', get_weather_forecast_area_by_first_letter))
    # app.add_handler(CommandHandler('rainfall_now', rainfall_now))

    # weather forecast conversations
    weather_forecast_conv_handler = ConversationHandler(
        entry_points=[CommandHandler('weather_forecast', get_weather_forecast_area_by_first_letter)],
        states={
            WF_FIRST_QUESTION: [CallbackQueryHandler(weather_forecast)],
            WF_SECOND_QUESTION: [CallbackQueryHandler(get_weather_forecast_by_area)]
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    app.add_handler(weather_forecast_conv_handler)


    # waiting for messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    # app.add_handler(CallbackQueryHandler(handle_buttons))

    # errors
    app.add_error_handler(error)

    # polling
    # checks every 5s for user response
    print("Polling")
    app.run_polling(poll_interval = 3)