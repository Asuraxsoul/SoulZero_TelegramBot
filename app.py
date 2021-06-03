import re
from flask import Flask, request
import telegram
from telebot.credentials import bot_token, bot_user_name, URL, my_chat_id

global bot
global TOKEN
global BOTNAME
global MY_CHAT_ID
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)
BOTNAME = bot_user_name
MY_CHAT_ID = my_chat_id

help_message = """/place to enquire Singapore's bouldering gyms categorized by locations,
/nearme to enquire Singapore bouldering gyms near me (if any, within 10km radius),
/gym_name to enquire more details about the gym,
/feedback to feedback inaccurate information provided or improvements to the bot,
/help to enquire on available commands."""
welcome_message = "Welcome to Boulder_SG @" + BOTNAME + ", this bot will help you to find a bouldering gym in " \
                  "Singapore!\n" + help_message
error_message = """Bot does not understand your input, please try typing /help for help"""

# start the flask app
app = Flask(__name__)


@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    # retrieve the message in JSON and then transform it to Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    chat_id = update.message.chat.id
    msg_id = update.message.message_id

    # Telegram understands UTF-8, so encode text for unicode compatibility
    text = update.message.text.encode('utf-8').decode()
    # for debugging purposes only
    print("got text message :", text)

    # the first time you chat with the bot AKA the welcoming message
    if text == "/start":
        # send the welcoming message
        bot.sendMessage(chat_id=chat_id, text=welcome_message)

    elif text == "/help":
        bot.sendMessage(chat_id=chat_id, text=help_message)

    elif text == "/feedback":
        bot.sendMessage(chat_id=chat_id, text="Please type in your feedback")

        # receive and record user feedback
        respond()
        feedback = update.message.text.encode('utf-8').decode()

        # message me the response
        bot.sendMessage(chat_id=MY_CHAT_ID, text="Feedback: " + feedback)
        bot.sendMessage(chat_id=chat_id, text="Thank you, your feedback has been recorded!")

    elif text == "/places":
        bot.sendMessage(chat_id=chat_id, text="Which part of Singapore are you looking at?")
        # activate choice
        # if north, south, east, west, central
        # then send the whole list of bouldering gyms

    elif text == "/nearme":
        bot.sendMessage(chat_id=chat_id, text="You are at xxx now, the nearest gyms (within 10km, if any) are xxx.")

    else:
        try:
            # clear the message we got from any non alphabets
            text = re.sub(r"\W", "_", text)
            # create the api link for the avatar based on http://avatars.adorable.io/
            url = "https://api.adorable.io/avatars/285/{}.png".format(text.strip())
            # reply with a photo to the name the user sent,
            # note that you can send photos by url and telegram will fetch it for you
            bot.sendPhoto(chat_id=chat_id, photo=url, reply_to_message_id=msg_id)
        except Exception:
            # if things went wrong
            bot.sendMessage(chat_id=chat_id,
                            text="There was a problem in the name you used, please enter different name",
                            reply_to_message_id=msg_id)

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
