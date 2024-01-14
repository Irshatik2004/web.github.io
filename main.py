import telebot
from telebot import types
from telebot.types import WebAppInfo

bot = telebot.TeleBot('6854505463:AAE-vVzQuaU0vT64vx-BlwQqGM3BrTnHJUQ')

@bot.message_handler(commands=['start'])
def start(message):
    knopka = types.ReplyKeyboardMarkup()
    btn1 = (types.KeyboardButton('Открыть веб страицу', web_app=WebAppInfo(url='https://irshatik2004.github.io/touch-.nojekyll/')))
    knopka.add(btn1)
    bot.send_message(message.chat.id, 'Привет мой друг', reply_markup=knopka)


bot.polling(non_stop=True)