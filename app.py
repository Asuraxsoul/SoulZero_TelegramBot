import json
from flask import Flask, request
import telegram
from telebot.credentials import bot_token, bot_user_name, URL, my_chat_id
from database.boulder_places import boulder_gyms
import math

global bot
global TOKEN
global BOTNAME
global MY_CHAT_ID
global all_boulder_places

TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)
BOTNAME = bot_user_name
MY_CHAT_ID = my_chat_id
all_boulder_places = json.loads(boulder_gyms)

isFeedback = False

help_message = """🗺 /places to enquire Singapore's bouldering gyms categorized by locations,
🤸 /all to see all available bouldering gyms in Singapore,
🎯 gym_name to enquire more details about the gym,
🧭 /nearby to enquire Singapore bouldering gyms near me (if any, within 5km radius),
📝 /feedback to feedback inaccurate information provided or improvements to the bot,
ℹ /help to enquire on available commands."""
welcome_message = "Welcome to Boulder_SG 🧗 @" + BOTNAME + ", this bot will help you to find a bouldering gym in " \
                                                           "Singapore!\n\n" + help_message
error_message = """Bot does not understand your input, please try typing /help to view commands"""

# start the flask app
app = Flask(__name__)


@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    # retrieve the message in JSON and then transform it to Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    location = update.message.location

    if location is not None:
        # Haversine Formula to calculate distance between 2 lat-lng points
        latitude = location.latitude
        longitude = location.longitude
        earth_radius = 6378.0
        within_distance = 5.0
        lat1 = math.radians(latitude)
        lng1 = math.radians(longitude)

        keyboard = [[]]
        keyboard_index = 0
        for gym_info in all_boulder_places['boulderGyms']:
            lat2 = math.radians(gym_info['lat'])
            lng2 = math.radians(gym_info['lng'])
            dlat = lat2 - lat1
            dlng = lng2 - lng1

            a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlng / 2) ** 2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            distance = earth_radius * c

            if distance <= within_distance:
                keyboard.insert(keyboard_index, [telegram.KeyboardButton(gym_info['name'])])

            keyboard_index = keyboard_index + 1
        reply_markup = telegram.ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)

        bot.sendMessage(chat_id=chat_id,
                        text="You are currently at " + "latitude: " + str(latitude) + ", longitude: "
                        + str(longitude) + ".\nThe nearest gyms (within 5km) are shown below, if any.",
                        reply_markup=reply_markup)

        return 'ok'

    else:
        # Telegram understands UTF-8, so encode text for unicode compatibility
        if update.message.text is None:
            return 'not ok'

        else:
            text = update.message.text.encode('utf-8').decode()
            print("got text message: ", text)


# feedback function ---------------------------------------------------------------------------------------------------
            global isFeedback
            print("isFeedback: ", isFeedback)
            if isFeedback:
                isFeedback = False
                feedback = "Feedback: " + text
                bot.sendMessage(chat_id=my_chat_id, text=feedback)
                bot.sendMessage(chat_id=chat_id, text="Thank you, your feedback has been recorded! 📝")

            elif text == "/feedback":
                isFeedback = True
                bot.sendMessage(chat_id=chat_id, text="Please type in your feedback")
# ---------------------------------------------------------------------------------------------------------------------

            elif text == "/start":
                bot.sendMessage(chat_id=chat_id, text=welcome_message)

            elif text == "/help":
                bot.sendMessage(chat_id=chat_id, text=help_message)

            elif text == "/all":
                keyboard = [[]]
                keyboard_index = 0
                for gym_info in all_boulder_places['boulderGyms']:
                    keyboard.insert(keyboard_index, [telegram.KeyboardButton(gym_info['name'])])
                    keyboard_index = keyboard_index + 1
                reply_markup = telegram.ReplyKeyboardMarkup(keyboard)

                bot.sendMessage(chat_id=chat_id,
                                text="Here are all the available bouldering gyms in Singapore",
                                reply_markup=reply_markup)

            elif text == "/places":
                keyboard = [[telegram.KeyboardButton('🔥 North')],
                            [telegram.KeyboardButton('🌊 North-East')],
                            [telegram.KeyboardButton('🎋 East')],
                            [telegram.KeyboardButton('🎐 West')],
                            [telegram.KeyboardButton('⛰ Central')]]
                reply_markup = telegram.ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)

                bot.sendMessage(chat_id=chat_id, text="Which part of Singapore are you looking at? 🌏",
                                reply_markup=reply_markup)
                # activate choice

# send the whole list of bouldering gyms based on north north-east east west central areas ----------------------------
            elif text == "🔥 North":
                keyboard = [[]]
                keyboard_index = 0
                for gym_info in all_boulder_places['boulderGyms']:
                    if gym_info['category'] == 'North':
                        keyboard.insert(keyboard_index, [telegram.KeyboardButton(gym_info['name'])])
                    keyboard_index = keyboard_index + 1
                reply_markup = telegram.ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)

                bot.sendMessage(chat_id=chat_id,
                                text="Here are the bouldering gyms located at the North\n/places to find other gyms",
                                reply_markup=reply_markup)

            elif text == "🌊 North-East":
                keyboard = [[]]
                keyboard_index = 0
                for gym_info in all_boulder_places['boulderGyms']:
                    if gym_info['category'] == 'North-East':
                        keyboard.insert(keyboard_index, [telegram.KeyboardButton(gym_info['name'])])
                    keyboard_index = keyboard_index + 1
                reply_markup = telegram.ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)

                bot.sendMessage(chat_id=chat_id,
                                text="Here are the bouldering gyms located at the North-East\n/places to find other "
                                     "gyms",
                                reply_markup=reply_markup)

            elif text == "🎋 East":
                keyboard = [[]]
                keyboard_index = 0
                for gym_info in all_boulder_places['boulderGyms']:
                    if gym_info['category'] == 'East':
                        keyboard.insert(keyboard_index, [telegram.KeyboardButton(gym_info['name'])])
                    keyboard_index = keyboard_index + 1
                reply_markup = telegram.ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)

                bot.sendMessage(chat_id=chat_id,
                                text="Here are the bouldering gyms located at the East\n/places to find other gyms",
                                reply_markup=reply_markup)

            elif text == "🎐 West":
                keyboard = [[]]
                keyboard_index = 0
                for gym_info in all_boulder_places['boulderGyms']:
                    if gym_info['category'] == 'West':
                        keyboard.insert(keyboard_index, [telegram.KeyboardButton(gym_info['name'])])
                    keyboard_index = keyboard_index + 1
                reply_markup = telegram.ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)

                bot.sendMessage(chat_id=chat_id,
                                text="Here are the bouldering gyms located at the West\n/places to find other gyms",
                                reply_markup=reply_markup)

            elif text == "⛰ Central":
                keyboard = [[]]
                keyboard_index = 0
                for gym_info in all_boulder_places['boulderGyms']:
                    if gym_info['category'] == 'Central':
                        keyboard.insert(keyboard_index, [telegram.KeyboardButton(gym_info['name'])])
                    keyboard_index = keyboard_index + 1
                reply_markup = telegram.ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)

                bot.sendMessage(chat_id=chat_id,
                                text="Here are the bouldering gyms located at the Central\n/places to find other gyms",
                                reply_markup=reply_markup)
# ---------------------------------------------------------------------------------------------------------------------

            elif text == "/nearby":
                keyboard = [[telegram.KeyboardButton('📍 Location', request_location=True)]]
                reply_markup = telegram.ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)

                bot.sendMessage(chat_id=chat_id,
                                text="Please enable location privacy for Telegram and provide your current location",
                                reply_markup=reply_markup)

            else:
                # for loop to find such a gym
                has_gym = False
                found_exact_gym = False
                has_gym_list = False

                keyboard = [[]]
                keyboard_index = 0
                for gym_info in all_boulder_places['boulderGyms']:
                    if gym_info['name'].lower() == text.lower():
                        has_gym = True
                        found_exact_gym = True
                        area = gym_info['category']
                        if area == "North":
                            area = " 🔥"
                        elif area == "North-East":
                            area = " 🌊"
                        elif area == "East":
                            area = " 🎋"
                        elif area == "West":
                            area = " 🎐"
                        elif area == "Central":
                            area = " ⛰"
                        caption = gym_info['name'] + area \
                                  + "\nLocation: " + gym_info['location'] \
                                  + "\nBooking: " + gym_info['booking'] \
                                  + "\nMore details: " + gym_info['url']

                        bot.sendPhoto(chat_id=chat_id, photo=open(gym_info['image'], 'rb'), caption=caption)
                        break

                    elif gym_info['name'].lower().startswith(text.lower()):
                        has_gym = True
                        has_gym_list = True

                        keyboard.insert(keyboard_index, [telegram.KeyboardButton(gym_info['name'])])
                        keyboard_index = keyboard_index + 1

                # if has a list of gyms and no exact gyms
                if has_gym_list and not found_exact_gym:
                    reply_markup = telegram.ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
                    bot.sendMessage(chat_id=chat_id,
                                    text="Here are the possible bouldering gyms you are searching for!",
                                    reply_markup=reply_markup)

                # no such command, error message
                if not has_gym:
                    bot.sendMessage(chat_id=chat_id, text=error_message)

            return 'ok'


# To check if heroku server is still hosting
@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    # we use the bot object to link the bot to our app which live
    # in the link provided by URL
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    # something to let us know things work
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"


@app.route('/')
def index():
    return '.'


if __name__ == '__main__':
    # note the threaded arg which allow
    # your app to have more than one thread
    app.run(threaded=True)
