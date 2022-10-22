import telebot

TOKEN = "1493436800:AAF1Eult9X13lyLQGGdScK63MbGOJyGqGbk"

bot = telebot.TeleBot(TOKEN)

bot.polling(none_stop=True)