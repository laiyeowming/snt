import telebot
import os

API_key = os.getenv('API_key')
bot = telebot.TeleBot("API_key")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, 5how are you doing?")

bot.polling()
