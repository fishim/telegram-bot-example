from telebot import types, telebot
from env.config import TgBot
from db import dbOperation

bot = telebot.TeleBot(str(TgBot.TELEGRAM_TOKEN))  # вказуємо токен бота

def on_startup():
    print('It is online')
    dbOperation.db_start()

@bot.message_handler(commands=['start'])
def main(message):  # функція для повернення команди
    if (not dbOperation.user_exist(message.chat.id)):
        dbOperation.add_user(message.chat.id, message.from_user.first_name)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('Surprise!')
    markup.add(btn1)
    bot.send_message(message.chat.id, message.text, reply_markup=markup)


@bot.message_handler(commands=['delete'])
def delete(message):
    bot.delete_message(message.chat.id, message.message_id - 1)



@bot.message_handler(content_types=['text'])
def mess(message):
    if message.chat.type == 'private':
        if message.text == 'Surprise!':
            photo = open('hello_world.png', 'rb')
            bot.send_photo(message.chat.id, photo)

@bot.message_handler(func=lambda message: True)         #функція для повернення повідомлення
def echo_all(message):
    bot.send_message(message.chat.id, message.text)


on_startup = on_startup()
bot.polling(skip_pending= True)

# Hello world
