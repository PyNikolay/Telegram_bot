import telebot

TOKEN = "YOUR TOKEN"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ['start'])
def hello(message):
	bot.send_message(message.chat.id, "Hello! Join in our TG Channel @SIG_devs")

bot.polling(non_stope=True)
