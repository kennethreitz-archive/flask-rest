# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

from .api import api

app.register_blueprint(api, url_prefix='/api')


if __name__ == '__main__':
    app.run()