import telebot

API_KEY = '1890951181:AAE7jafAINXxR1GZ-1TRA_a2r2Ip0h13Z0s'
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['greet'])
def greet(message):
    bot.reply_to(message, 'Hey! hows it going?')


@bot.message_handler(commands=['hi'])
def greet(message):
    bot.send_message(message.chat.id, 'Hi welcome!')


def rand_function(message):
    request = message.text.split()
    if len(request) < 2 or request[0].lower() not in 'price':
        return False
    else:
        return True


@bot.message_handler(func=rand_function)
def send_price(message):
    bot.send_message(message.chat.id, 'yay!')


bot.polling()
