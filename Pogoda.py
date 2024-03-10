import pyowm
import telebot

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils import config as cfg

config = cfg.get_default_config()
config['language'] = 'ru'

bot = telebot.TeleBot("5764001715:AAGvEzTeia6_EVVxCkAjtcc6h6TLC_ERS6c")
owm = OWM('559d785c65f32083647437dc35398607', config)
mgr = owm.weather_manager()

# Search for current weather in London (Great Britain) and get details

place = input("В каком город/стране?: ")

observation = mgr.weather_at_place(place)
w = observation.weather
temp = w.temperature('celsius')["temp"]

print( "В городе " + place + " сейчас " + str(w.detailed_status) + "!")
print( "Температура сейчас в районе " + str(temp))

if temp < 10:
    print( "Сейчас ппц как холодно, одевай кальсоны!")
elif temp < 20:
    print( "Сейчас прохладно, возьми с собой кофту или куртку!")
else:
    print( "Сегодня теплая погода, куртку можно не брать!")