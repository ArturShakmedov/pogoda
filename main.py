import telebot
from pogoda import weather_check


API_TOKEN = 'TOKEN'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Ты запустил телеграм бота прогноз погоды')
    _ = bot.send_message(message.chat.id, 'Введите город: ')
    bot.register_next_step_handler(_, pogoda)


def pogoda(message):
    citi = message.text
    forecast = weather_check(f'{citi} погода на русском')
    bot.send_message(message.chat.id, forecast)


bot.infinity_polling()
