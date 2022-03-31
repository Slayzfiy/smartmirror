# Ideas
# Teams (HW & Messages)
# WebUntis (HW & Timetable)
# Discord (Messages)
# Weather (Images: Clouds)
# News (Upday)
#
# Sudoku or modules games
import asyncio
import threading
import time

from FlaskManager import FlaskManager
from static.modules.animator.animator import Animator
from static.modules.mail.mail import Mail
from static.modules.quotes.quotes import Quotes
from static.modules.clock.clock import Clock
from static.modules.stocks.stocks import Stocks
from static.modules.todo.to_do import ToDoManager
from static.modules.weather.weather import Weather
from static.modules.voicinger.voicinger import Voicinger


class Mirror:
    def __init__(self):
        self.FlaskManager = None
        self.Clock = Clock('clock')
        self.ToDoManager = ToDoManager('todo')
        self.Weather = Weather('weather')
        self.Quotes = Quotes('quotes')
        self.Mail = Mail('mail')
        self.Stocks = Stocks('stocks')
        self.Animator = Animator('animator')
        self.Voicinger = None

        modules = {
            "clock": self.Clock,
            "todo": self.ToDoManager,
            "weather": self.Weather,
            "quotes": self.Quotes,
            "mail": self.Mail,
            "stocks": self.Stocks,
            "animator": self.Animator,
        }

        self.FlaskManager = FlaskManager(modules)

    def run(self):
        self.FlaskManager.run()

    def start_voice(self):
        self.Voicinger = Voicinger('voicinger')

        while 1:
            result = self.Voicinger.record_voice()
            self.FlaskManager.socketio.emit("trigger_focus_animation", {"module": result})
            time.sleep(1)


if __name__ == '__main__':
    mirror = Mirror()
    t1 = threading.Thread(target=mirror.run)
    t2 = threading.Thread(target=mirror.start_voice)

    t1.start()
    t2.start()

#     thread1 = webserver
#     thread2 = mikrofon im Hintergrund
