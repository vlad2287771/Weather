#pogodabybot

import telebot
from pyowm import OWM
from pyowm.utils.config import get_default_config

owm = OWM('f70322f96519f632b7ab71db9771c083')
mgr = owm.weather_manager()
config_dict = get_default_config()
config_dict['language'] = 'ru'

bot = telebot.TeleBot("5155363126:AAEQ7sEKGZWhAVAbHi8PSXxWvzFtPLHeyrA")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = mgr.weather_at_place(message.text)
	w = observation.weather
	temp = (w.temperature('celsius'))['temp']
	answer = "В городе " + message.text + " сейчас " + w.detailed_status + "\n"
	answer += "Температура  " + str(temp) + "\n"
	answer += "Скорость ветра  " + str(w.wind()['speed']) + "\n"
	answer += "Влажность  " + str(w.humidity) + "%" + "\n" + "\n"

	if 0 < temp < 10:
		answer += "На улице холодно одевайтесь теплее" + "\n"
	elif temp >= 10:
		answer += "На улице прохладно одевайтесь легче" + "\n"
	elif temp >= 19:
		answer += "На улице тепло одевайтесь легко" + "\n"
	elif temp <= 0:
		answer += "На улице очень холодно одевайтесь тепло" + "\n"



	bot.send_message(message.chat.id, answer)



bot.infinity_polling()
