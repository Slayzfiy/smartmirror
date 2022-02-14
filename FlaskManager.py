import json
import os
from urllib.parse import unquote

from flask import Flask, render_template, request, redirect, flash, get_flashed_messages, send_file, current_app, \
    send_from_directory, url_for

import json

from werkzeug.utils import secure_filename


class FlaskManager:
    def __init__(self, modules):
        self.app = Flask(
            static_folder='static',
            import_name='app',
            template_folder='flask_templates'
        )

        self.modules = modules
        self.app.debug = True
        self.setup_functions()
        self.app.run(host="0.0.0.0", port=1080, debug=True, use_reloader=True)

    def setup_functions(self):
        @self.app.route('/')
        def index_html():
            return render_template('subsitesModules/index.html', modules=self.modules)

        @self.app.route('/config', methods=["GET", "POST"])
        def handle_config():
            if request.method == "POST":
                form = request.form
                print(form)
                self.modules[form['formModule']].handle_post_method(form)  # passes the form data to the right module

            if request.method == "GET":
                modules_config = []

                for x in self.modules:
                    modules_config.append({x: self.modules[x].fetch_config()})

                # DEBUGGING #
                print(json.dumps({"global_module_config": modules_config}))

                return json.dumps({"global_module_config": modules_config})

            return "200"

        @self.app.route('/import_config', methods=["GET", "POST"])
        def import_config():
            if 'file' not in request.files:
                print("here")
                return "fehler", 200



        @self.app.route('/dashboard.html')
        def dashboard():
            return render_template('subsitesConfig/dashboard.html', modules=self.modules)

        @self.app.route('/clock', methods=["GET", "POST"])
        def clock():
            return render_template('subsitesConfig/clock.html', modules=self.modules)

        @self.app.route('/weather', methods=["GET", "POST"])
        def weather():
            if request.method == "GET":
                response = self.modules['weather'].handle_get_method(request.args)
                print(response)
                if response:
                    return response

            return render_template('subsitesConfig/weather.html', modules=self.modules)

        @self.app.route('/todo', methods=["GET", "POST"])
        def todo():
            print(request.form)
            if request.method == "POST":
                try:
                    self.modules['todo'].delete_todo(request.form['index'])
                except:
                    pass

                try:
                    self.modules['todo'].add_todo(request.form['data'])
                except:
                    pass

            if request.method == "GET":
                response = self.modules['todo'].handle_get_method(request.args)
                if response:
                    return response

            return render_template('subsitesConfig/todo.html', modules=self.modules)

        @self.app.route('/quotes', methods=["GET", "POST"])
        def quotes():
            if request.method == "GET":
                response = self.modules['quotes'].handle_get_method(request.args)
                print(response)
                if response:
                    return response

            return render_template('subsitesConfig/quotes.html', modules=self.modules)

        @self.app.route('/stocks', methods=["GET", "POST"])
        def stocks():
            if request.method == "GET":
                response = self.modules['stocks'].handle_get_method(request.args)
                if response:
                    return response

            if request.method == "POST":
                self.modules['stocks'].handle_post_method_module(request.form)

            return render_template('subsitesConfig/stocks.html', modules=self.modules)

        @self.app.route('/mail', methods=["GET", "POST"])
        def mail():
            if request.method == "POST":
                if self.modules['mail'].handle_post_method(request.form):
                    return render_template('subsitesConfig/mail.html', modules=self.modules), 201
                else:
                    return render_template('subsitesConfig/mail.html', modules=self.modules), 400

            if request.method == "GET":
                response = self.modules['mail'].handle_get_method(request.args)

                if response:
                    return response
                else:
                    pass

            return render_template('subsitesConfig/mail.html', modules=self.modules)

        @self.app.route("/config.html", methods=["POST"])
        def handle():
            try:
                if request.form["module"] in self.modules:
                    response = self.modules[request.form["module"]].handle(request)
                    if response:
                        return response
                    print(response)
            except Exception as ex:
                print("crashed: " + str(ex))
            return '', 204  # Default response

        @self.app.route('/config.html', methods=['GET'])
        def configuration_html():
            return render_template('config.html', modules=self.modules)
