from static.modules.module import *
import json


class ToDoManager(Module):
    def __init__(self, directory_path):
        super().__init__(directory_path)
        self.config = json.load(open(self.path_helper("config.json"), "r"))

    # handle POST method (AJAX)
    def handle_post_method(self, data):
        self.handle_default_conf(data)  # every time the same config files

    # handle GET method (AJAX)
    def handle_get_method(self, data):
        if data:
            if data["type"] == "fetch_todo":
                try:
                    a = json.dumps({"todo_entries": self.fetch_todo()})  # list as return type is not allowed
                    return a

                except:
                    return False

    def fetch_todo(self):
        return self.config['module_config']['entries']

    def delete_todo(self, index):
        try:
            self.config['module_config']['entries'].pop(int(index))
        except werkzeug.exceptions.BadRequestKeyError:
            pass

        self.save_config()

    def add_todo(self, data):
        self.config['module_config']['entries'].append(data)
        self.save_config()

    # def get_config_html(self):
    #     return self.generate_config_html({
    #         ":::REPLACE_TODOENTRIES:::": self.generate_entry_configuration_html()
    #     })
    #
    # def get_module_html(self):
    #     return self.generate_module_html({
    #         ":::REPLACE_TODOENTRIES:::": self.generate_entry_index_html()
    #     })
    #
    # def generate_entry_configuration_html(self):
    #     html = str()
    #     for entry in self.config['entries']:
    #         html += f'<li class="mt-3 deleteItem"><div class="form"><label class="form-check-label toDoItem"><a>' \
    #                 f'{entry}</a></label></div></li>'
    #     return html

    # def generate_entry_index_html(self):
    #     html = str()
    #     index = 0
    #     for entry in self.config['entries']:
    #         if index < 6:
    #             html += f'<li class="list-group-item bg-dark mb-1"><a>{entry}</a></li>'
    #             index += 1
    #         else:
    #             break
    #     return html

    # def generate_configuration_html(self):
    #     configuration_html = open("modules/todo/config.html", "r").read()
    #     return configuration_html.replace(':::REPLACEMARKER:::', ''.join(self.generate_entry_configuration_html()))
