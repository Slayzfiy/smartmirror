from static.modules.module import *
import requests


class Weather(Module):
    def __init__(self, directory_path):
        super().__init__(directory_path)
        self.config = json.load(open(self.path_helper("config.json"), "r"))

        self.location = self.config['module_config']['location']
        self.api_key = self.config['module_config']['api_key']

    def handle_post_method(self, data):
        self.handle_default_conf(data)
        self.config['module_config']['api_key'] = data['api_key']
        self.config['module_config']['location'] = data['location']

    def handle_get_method(self, data):
        if data:
            if data["type"] == "fetch_weather":
                try:
                    return json.dumps(self.fetch_weather_data())
                except:
                    return False


    def fetch_weather_data(self):
        uri = f'https://api.openweathermap.org/data/2.5/weather?units=metric&q={self.location}&appid={self.api_key}'
        response = requests.get(uri).json()
        weather_main = response['weather'][0]['main']
        weather_description = response['weather'][0]['description']
        weather_temp = response['main']['temp']
        weather_country = response['sys']['country']
        weather_city = response['name']
        weather_icon = response['weather'][0]['icon']
        return {
            "weather": weather_main,
            "description": weather_description,
            "temp": str(round(weather_temp)),
            "country": weather_country,
            "city": weather_city,
            "icon": f'https://s3-us-west-2.amazonaws.com/s.cdpn.io/162656/{weather_icon}.svg'
        }

    def generate_configuration_html(self):
        configuration_html = open("modules/weather/config.html", "r").read()
        if self.api_key is not None:
            configuration_html = configuration_html.replace(':::REPLACE_APIKEY:::', self.api_key)

        if self.location is not None:
            configuration_html = configuration_html.replace(':::REPLACE_LOCATION:::', self.location)

        return configuration_html

