from telebot import types, telebot
from env.config import TgBot
from db import dbOperation

bot = telebot.TeleBot(str(TgBot.TELEGRAM_TOKEN))  # вказуємо токен бота

def on_startup():
    print('It is online')
    dbOperation.db_start()


@bot.message_handler(commands=['start'])
def main(message):  # функція для повернення команди
    dbOperation.save_message(message)
    if (not dbOperation.user_exist(message.chat.id)):
        dbOperation.add_user(message.chat.id, message.from_user.first_name)
        send_mess = f"Hi, you're new here!"
    else:
        send_mess = f"Hi, <b>{message.from_user.first_name}</b>! Nice to see you again."
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('Surprise!')
    btn2 = types.KeyboardButton('History')
    markup.add(btn1, btn2)

    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['delete'])
def delete(message):
    dbOperation.save_message(message)
    bot.delete_message(message.chat.id, message.message_id - 1)

@bot.message_handler(content_types=['text'])
def mess(message):
    dbOperation.save_message(message)
    if message.chat.type == 'private':
        if message.text == 'Surprise!':
            photo = open('hello_world.png', 'rb')
            bot.send_photo(message.chat.id, photo)
        elif message.text == 'History':
            rows = dbOperation.get_chat_history(message)
            response = "Your chat history:"
            if len(rows) == 0:
                bot.reply_to(message, "Історія чату порожня.")

            else:
                for row in rows:
                    username = row[1]
                    message_text = row[2]
                    date = row[3].strftime("%Y-%m-%d %H:%M:%S")
                    response += f"\n{date} - {username}: {message_text}"
                bot.send_message(message.chat.id, response)
        else:
            echo_all(message)


#@bot.message_handler(func=lambda message: True)    #функція для повернення повідомлення
def echo_all(message):
    bot.send_message(message.chat.id, message.text)


on_startup = on_startup()
bot.polling(skip_pending= True)

# Hello world
