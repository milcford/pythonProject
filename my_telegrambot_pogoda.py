import pyowm
import telebot

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils import config as cfg

# В конфигурации указываем язык русский для модуля погоды
config = cfg.get_default_config()
config['language'] = 'ru'

bot = telebot.TeleBot("5764001715:AAGvEzTeia6_EVVxCkAjtcc6h6TLC_ERS6c")
owm = OWM('559d785c65f32083647437dc35398607', config)
mgr = owm.weather_manager()

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = mgr.weather_at_place( message.text )
    w = observation.weather
    temp = w.temperature('celsius')["temp"]

    answer = "В городе " + message.text + " сейчас " + str(w.detailed_status) + "!" + "\n"
    answer += "Температура в районе " + str(temp) + "\n\n"

    if temp < 10:
        answer += "Сейчас ппц как холодно, лучше одеться потеплее!"
    elif temp < 20:
        answer += "Сейчас прохладно, возьми с собой куртку!"
    else:
        answer += "Сегодня теплая погода, куртку можно не брать!"


    bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True )