import telebot

bot = telebot.TeleBot('5887488636:AAEtc9otfhVPvaOOOrazVPOJeUKyKCFFiPA')#вказуємо токен бота 

@bot.message_handler(commands=['start'])
def main(message):                                         #функція для повернення команди 
    bot.send_message(message.chat.id, message.text)

@bot.message_handler(func=lambda message: True)
def echo_all(message):                                     #функція для повернення повідомлення
	bot.send_message(message.chat.id, message.text)

bot.infinity_polling()