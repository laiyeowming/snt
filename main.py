""" .py for first telegram bot"""

import telebot

TOKEN = '1790716225:AAHSdpfgFMSX7dlCVgBuu_gZyNu-LYeo0ng'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['hello', 'help'])

def send_welcome(message):
    '''returns msg from /hello and /help'''
    bot.reply_to(message, "Howdy, how are you doing?")

bot.polling()
