# from modules.module import Module
import json

import werkzeug.exceptions
import os
from ..module import Module


class Clock(Module):
    def __init__(self, directory_path):
        super().__init__(directory_path)
        self.config = json.load(open(self.path_helper('config.json'), 'r'))

    def handle_post_method(self, data):
        self.handle_default_conf(data)  # every time the same config files
        self.config['module_config'] = {
            "timezone": data['timezone'],
            "clock_background_color": data['clock_background_color'],
            "pointer_color": data['pointer_color'],
            "number_color": data['number_color']
        }
        self.save_config()

    def handle(self, data):
        # self.config['design'][0]['background-color'] = data['background-color']
        # self.config['design'][0]['pointer-color'] = data['pointer-color']
        # self.config['design'][0]['number-color'] = data['number-color']
        # self.config['timezone'] = data['timezone']
        # try:
        #     self.config['visibility'] = data['visibility']
        #     self.visibility = data['visibility']
        # except werkzeug.exceptions.BadRequestKeyError:
        #     self.config['visibility'] = "off"
        #     self.visibility = "off"
        #
        # # we need to assign the current Clock object the new values, cuz only at start it takes the values from config
        # self.design = {
        #     "background-color": data["background-color"],
        #     "pointer-color": data["pointer-color"],
        #     "number-color": data["number-color"]
        # }
        # self.timezone = data['timezone']
        # self.save_config()
        pass
        # print(f'saved following settings {self.design}, timezone: {self.timezone}, visibility: {self.visibility}')

