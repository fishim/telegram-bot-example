import telebot
from telebot import types
from config import TgBot
bot = telebot.TeleBot(str(TgBot.TELEGRAM_TOKEN))#вказуємо токен бота

@bot.message_handler(commands=['start'])
def main(message):                                         #функція для повернення команди
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('Surprise!')
    markup.add(btn1)
    bot.send_message(message.chat.id, message.text, reply_markup=markup)

@bot.message_handler(commands=['delete'])
def delete(message):
    bot.delete_message(message.chat.id, message.message_id - 1)

# @bot.message_handler(func=lambda message: True)
# def echo_all(message):                                     #функція для повернення повідомлення
# 	bot.send_message(message.chat.id, message.text)

@bot.message_handler(content_types=['text'])
def mess(message):
    if message.chat.type == 'private':
        if message.text == 'Surprise!':
            photo = open('hello_world.png', 'rb')
            bot.send_photo(message.chat.id, photo)




bot.infinity_polling()