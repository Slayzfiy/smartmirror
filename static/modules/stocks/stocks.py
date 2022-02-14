from static.modules.module import *
import yfinance as yf


class Stocks(Module):
    def __init__(self, directory_path):
        super().__init__(directory_path)
        # self.config = json.load(open(self.path_helper('config.json'), 'r'))
        self.watchlist = self.config['module_config']['watchlist']

    def handle_post_method(self, data):
        self.handle_default_conf(data)  # every time the same config files
        self.config['module_config']['currency'] = data['currency']
        self.save_config()

    def handle_get_method(self, data):
        if data:
            if data["type"] == "fetch_stocks":
                try:
                    stock = StockData(self.watchlist[0])
                    print(stock.stock_json())
                    return stock.stock_json()

                except:
                    return False

    def handle_post_method_module(self, data):
        if data.get('tagToRemove'):
            self.watchlist.remove(data.get('tagToRemove'))

        elif data.get('stockToAdd'):
            self.watchlist.append(data.get('stockToAdd'))

        self.save_config()

    @staticmethod
    def generate_configuration_html(self):
        configuration_html = open("modules/stocks/config.html", "r").read()
        return configuration_html


class StockData:
    def __init__(self, stock):
        self.stock = stock
        self.current_price, self.yesterdays_price, self.logo, self.difference_in_percent, self.currency = None, None, None, None, None
        self.fetch_stock()

    def fetch_stock(self):
        ticker = yf.Ticker(self.stock).info
        self.current_price = ticker['regularMarketPrice']
        self.yesterdays_price = ticker['previousClose']
        self.logo = ticker['logo_url']
        self.difference_in_percent = round((((self.current_price / self.yesterdays_price) - 1) * 100), 2)
        self.currency = ticker['currency']

    def stock_json(self):
        return json.dumps({"stock": {
            "name": self.stock,
            "current_price": self.current_price,
            "yesterdays_price": self.yesterdays_price,
            "difference_in_percent": self.difference_in_percent,
            "currency": self.currency,
            "logoURI": self.logo
        }})
