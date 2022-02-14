import json
import os

import werkzeug.exceptions
import os


class Module:
    def __init__(self, module_name):
        self.module_name = module_name
        self.config = json.load(open(self.path_helper("config.json"), "r"))

    def handle_default_conf(self, data):
        # we need to assign the current Clock object the new values, cuz only at start it takes the values from config
        visibility = None
        try:
            visibility = data["visibility"]

        except werkzeug.exceptions.BadRequestKeyError:
            # because if toggler in html is not checked, it won't send a value
            visibility = "off"

        self.config['general_config'] = {
            "visibility": visibility,
            "grid_place": data['grid_system']
        }

        self.config['design_config'] = {
            "font_size": data['font_size'],
            "font_family": data['font_family'],
            "background_color": data['background_color'],
        }

        self.save_config()

    def fetch_config(self):
        return self.config

    def export_config_data(self):
        return

    def alter_config(self, key, value):
        self.config[key] = value
        with open(self.path_helper('config.json'), 'w') as file:
            json.dump(self.config, file)
            file.close()

    def path_helper(self, file):
        dirname = os.path.dirname(__file__)
        path = f"static/modules/{self.module_name}/{file}"
        return path

    @staticmethod
    def __generate_html(file, replace_dict):
        temp = file
        if replace_dict:
            for x in replace_dict:
                temp = temp.replace(x, replace_dict[x])
        return temp

    def save_config(self):
        with open(self.path_helper("config.json"), 'w') as file:
            json.dump(self.config, file, indent=3)
            file.close()
