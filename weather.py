from pyowm import OWM
from pyowm.utils.config import get_default_config

owm = OWM('f70322f96519f632b7ab71db9771c083')
mgr = owm.weather_manager()

config_dict = get_default_config()
config_dict['language'] = 'ru'

place = input("Введите ваш город?")

observation = mgr.weather_at_place(place)
w = observation.weather
temp = (w.temperature('celsius'))['temp']

print("В городе " + place + " сейчас " + w.detailed_status)
print("Температура " + str(temp))
print("Скорость ветра " + str(w.wind()['speed']))
print("Влажность " + str(w.humidity) + "%")

if 0 < temp < 10:
    print("На улице холодно одевайтесь теплее")
elif temp >= 10:
    print("На улице прохладно одевайтесь легче")
elif temp >= 19:
    print("На улице тепло одевайтесь легко")
elif temp <= 0:
    print("На улице очень холодно одевайтесь тепло")
