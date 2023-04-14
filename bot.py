import telebot

bot = telebot.TeleBot('5831486734:AAGLPj77zzky_CZO7cvygiFnnT7GwmJyUaY')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, message.text)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.send_message(message.chat.id, message.text)

bot.infinity_polling()