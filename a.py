import telebot

# Insert your Telegram Bot API token here
TOKEN = '7250423999:AAH2dBM2iLd_P4FAXgYfMFkbjNQp7wu1YIE'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hello! I am your Telegram Bot.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()

