import telebot
TOKEN = '1790716225:AAHSdpfgFMSX7dlCVgBuu_gZyNu-LYeo0ng'
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['hello', 'help'])
def send_welcome(message): bot.reply_to(message, "Howdy, how are you doing?")
bot.polling()
