import random

from static.modules.module import *
import werkzeug.exceptions


class Quotes(Module):
    def __init__(self, directory_path):
        super().__init__(directory_path)
        self.config = json.load(open(self.path_helper("config.json"), "r"))
        self.quotes = json.load(open(self.path_helper("quotes.json"), "r"))
        # self.quotes = json.load(open(self.path_helper("quotes.json"), "r"))
        # self.module_html = open(self.path_helper("module.html"), "r").read()
        # self.config_html = open(self.path_helper("config.html"), "r").read()
        # self.visibility = self.config['visible']
        # self.maxQuoteLength = self.config['maxQuoteLength']

    def handle_post_method(self, data):
        self.handle_default_conf(data)
        self.config['module_config']['max_quote_length'] = data['max_quote_length']

    def handle_get_method(self, data):
        if data:
            if data["type"] == "fetch_quote":
                try:
                    return self.fetch_all_quotes(limiter=1)
                except:
                    return False

    def fetch_author_list(self):
        authors = [x['author'] for x in self.quotes]
        print(authors)

    def fetch_all_quotes(self, limiter=None):
        return json.dumps({"quote": self.quotes[0]})

    def handle(self, data):
        self.config['maxQuoteLength'] = data['quoteLength']
        self.maxQuoteLength = data['quoteLength']
        try:
            self.config['visibility'] = data['visibility']
            self.visibility = data['visibility']
        except werkzeug.exceptions.BadRequestKeyError:
            self.config['visibility'] = "off"
            self.visibility = "off"

        self.save_config()
        print(f'saved following settings max quote length: {self.maxQuoteLength}, visibility: {self.visibility}')

    def fetch_quote(self, author=None, max_length=200):
        if author:
            quote = [x for x in self.quotes if x['author'] == author and len(x['text'].split(' ')) < max_length]
            if quote:
                return random.choice(quote)
            else:
                return None
        else:
            return random.choice([x for x in self.quotes if len(x['text'].split(' ')) < max_length])

    def get_config_html(self):
        return self.generate_config_html({
            ":::REPLACE_BOOL:::": ("checked" if self.config["visible"] else "")
        })

    def get_module_html(self):
        if self.config["visible"]:
            quote = self.fetch_quote()
            text = quote['text']
            author = quote['author']
            if not author:
                author = "Unknown"

            return self.generate_module_html({
                ":::REPLACE_QUOTE:::": text,
                ":::REPLACE_AUTHOR:::": author
            })
        else:
            return ""
