from datetime import datetime, timezone
from static.modules.module import *
from imap_tools import MailBox
import requests


class Mail(Module):
    def __init__(self, directory_path):
        super().__init__(directory_path)
        self.config = json.load(open(self.path_helper("config.json"), "r"))
        self.email, self.password, self.imap, self.port = None, None, None, None
        self.override_session_config()

    def override_session_config(self):
        self.email = self.config['module_config']['mail']['email']
        self.password = self.config['module_config']['mail']['password']
        self.imap = self.config['module_config']['mail']['mail_server']
        self.port = self.config['module_config']['mail']['port']

    def handle_post_method(self, data):
        self.handle_default_conf(data)

        # if user changes settings, but doesn't enter the password again, the password won't be sent to the backend
        if data["password"]:
            self.config['module_config']['mail'] = {
                "email": data['email'],
                "password": data['password'],
                "mail_server": data['mail_server'],
                "port": data['port']
            }
        else:
            self.config['module_config']['mail'] = {
                "email": data['email'],
                "password": self.config['module_config']['mail']['password'],
                "mail_server": data['mail_server'],
                "port": data['port']
            }

        self.save_config()
        self.override_session_config()

    def handle_get_method(self, data):
        if data:
            if data["type"] == "check_connection":
                try:
                    mailer = Mailer(data['email'], data['password'], data['mail_server'], data['port'])
                    return mailer.fetch_latest_mails()
                except:
                    return False

            if data["type"] == "fetch_mails":
                try:
                    mailer = Mailer(self.email, self.password, self.imap, self.port)
                    return mailer.fetch_latest_mails()
                except Exception as ex:
                    return False

    # @staticmethod
    # def imap_server_finder(email):
    #     settings = requests.get(f'https://emailsettings.firetrust.com/settings?q={email}').json()['settings']
    #     address = settings[1]['address']
    #     port = settings[1]['port']
    #
    #     return {
    #         "address": address,
    #         "port": port
    #     }


class Mailer:
    def __init__(self, email, password, address, port):
        self.email = email
        self.password = password
        self.address = address
        self.port = port

    def fetch_latest_mails(self):
        msg = MailBox(self.address).login(self.email, self.password, 'INBOX').fetch(limit=3, reverse=True)
        mails = {"mails": []}
        for i, x in enumerate(msg):
            mails["mails"].append(
                {
                    "subject": (str(x.subject[0:45] + "...") if len(x.subject) > 45 else x.subject),
                    "date": x.date.strftime("%d.%m.%Y, %H:%M"),
                    "from": x.from_[x.from_.find('@') + 1:]
                }
            )
        # int((datetime.now(timezone.utc) - x.date).total_seconds() / 60) -> in order to get the AGO time

        return json.dumps(mails)
