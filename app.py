# Ideas
# Teams (HW & Messages)
# WebUntis (HW & Timetable)
# Discord (Messages)
# Weather (Images: Clouds)
# News (Upday)
#
# Sudoku or modules games


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
        self.Clock = Clock('clock')
        self.ToDoManager = ToDoManager('todo')
        self.Weather = Weather('weather')
        self.Quotes = Quotes('quotes')
        self.Mail = Mail('mail')
        self.Stocks = Stocks('stocks')
        self.Animator = Animator('animator')
        self.Voicinger = Voicinger('voicinger')
        modules = {
            "clock": self.Clock,
            "todo": self.ToDoManager,
            "weather": self.Weather,
            "quotes": self.Quotes,
            "mail": self.Mail,
            "stocks": self.Stocks,
            "animator": self.Animator,
            "voicinger": self.Voicinger
        }
        FlaskManager(modules)


if __name__ == '__main__':
    mirror = Mirror()
