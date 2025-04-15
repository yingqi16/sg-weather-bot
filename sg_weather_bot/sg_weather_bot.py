from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler, CallbackContext, ConversationHandler
from dotenv import load_dotenv
import os
from pathlib import Path
import requests

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

def clean_date(date):
    return date.replace('+08:00', '').replace('T', ' ')

# query api
def get_weather_details(area):

    url = "https://api-open.data.gov.sg/v2/real-time/api/two-hr-forecast"

    response = requests.get(url)
    retrieve_key_info = response.json()['data']['items'][0]
    update_time = retrieve_key_info['update_timestamp']
    valid_forecast_period = retrieve_key_info['valid_period']
    start_forecast_period = valid_forecast_period['start']
    end_forecast_period = valid_forecast_period['end']
    forecast_all_area = retrieve_key_info['forecasts']

    area_of_interest = area.replace('_weather_forecast', '').lower().strip()

    forecast_area = None
    for data in forecast_all_area:
        if data['area'].lower().strip() == area_of_interest:
            forecast_area = data['forecast']
            break
    return clean_date(update_time), clean_date(start_forecast_period), clean_date(end_forecast_period), forecast_area, area_of_interest


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
        [InlineKeyboardButton("Ang Mo Kio", callback_data='Ang Mo Kio_weather_forecast')],
        [InlineKeyboardButton("Bedok", callback_data='Bedok_weather_forecast')],
        [InlineKeyboardButton("Bishan", callback_data='Bishan_weather_forecast')],
        [InlineKeyboardButton("Boon Lay", callback_data='Boon Lay_weather_forecast')],
        [InlineKeyboardButton("Bukit Batok", callback_data='Bukit Batok_weather_forecast')],
        [InlineKeyboardButton("Bukit Merah", callback_data='Bukit Merah_weather_forecast')],
        [InlineKeyboardButton("Bukit Panjang", callback_data='Bukit Panjang_weather_forecast')],
        [InlineKeyboardButton("Bukit Timah", callback_data='Bukit Timah_weather_forecast')],
        [InlineKeyboardButton("Central Water Catchment", callback_data='Central Water Catchment_weather_forecast')],
        [InlineKeyboardButton("Changi", callback_data='Changi_weather_forecast')],
        [InlineKeyboardButton("Choa Chu Kang", callback_data='Choa Chu Kang_weather_forecast')],
        [InlineKeyboardButton("City", callback_data='City_weather_forecast')],
        [InlineKeyboardButton("Clementi", callback_data='Clementi_weather_forecast')]]
    elif query.data == 'E_J_weather_forecast':
        buttons = [
        [InlineKeyboardButton("Geylang", callback_data='Geylang_weather_forecast')],
        [InlineKeyboardButton("Hougang", callback_data='Hougang_weather_forecast')],
        [InlineKeyboardButton("Jalan Bahar", callback_data='Jalan Bahar_weather_forecast')],
        [InlineKeyboardButton("Jurong East", callback_data='Jurong East_weather_forecast')],
        [InlineKeyboardButton("Jurong Island", callback_data='Jurong Island_weather_forecast')],
        [InlineKeyboardButton("Jurong West", callback_data='Jurong West_weather_forecast')]]
    elif query.data == 'K_N_weather_forecast':
        buttons = [
            [InlineKeyboardButton("Kallang", callback_data='Kallang_weather_forecast')],
            [InlineKeyboardButton("Lim Chu Kang", callback_data='Lim Chu Kang_weather_forecast')],
            [InlineKeyboardButton("Mandai", callback_data='Mandai_weather_forecast')],
            [InlineKeyboardButton("Marine Parade", callback_data='Marine Parade_weather_forecast')],
            [InlineKeyboardButton("Novena", callback_data='Novena_weather_forecast')]
        ]
    elif query.data == 'O_R_weather_forecast':
        buttons = [
            [InlineKeyboardButton("Pasir Ris", callback_data='Pasir Ris_weather_forecast')],
        [InlineKeyboardButton("Paya Lebar", callback_data='Paya Lebar_weather_forecast')],
        [InlineKeyboardButton("Pioneer", callback_data='Pioneer_weather_forecast')],
        [InlineKeyboardButton("Pulau Tekong", callback_data='Pulau Tekong_weather_forecast')],
        [InlineKeyboardButton("Pulau Ubin", callback_data='Pulau Ubin_weather_forecast')],
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
        [InlineKeyboardButton("Southern Islands", callback_data='Southern Islands_weather_forecast')],
        [InlineKeyboardButton("Sungei Kadut", callback_data='Sungei Kadut_weather_forecast')],
        [InlineKeyboardButton("Tampines", callback_data='Tampines_weather_forecast')],
        [InlineKeyboardButton("Toa Payoh", callback_data='Toa Payoh_weather_forecast')],
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
    update_time, start_forecast_period, end_forecast_period, forecast_area, area_of_interest = get_weather_details(response)

    await query.message.reply_text(f"Hello! The weather at {area_of_interest} is {forecast_area}. Data is updated on {update_time}, forecast between {start_forecast_period} and {end_forecast_period}")
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