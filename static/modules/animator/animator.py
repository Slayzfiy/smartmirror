# from modules.module import Module
import json

import werkzeug.exceptions
import os
from ..module import Module


class Animator(Module):
    def __init__(self, directory_path):
        super().__init__(directory_path)
        self.config = json.load(open(self.path_helper('config.json'), 'r'))

    def handle_post_method(self, data):
        self.handle_default_conf(data)  # every time the same config files
        self.config['module_config'] = {
            "image_source": data["image_source"]
        }
        self.save_config()

    def handle_get_method(self, data):
        if data:
            if data["type"] == "fetch_image":
                return self.config['module_config']["image_source"]