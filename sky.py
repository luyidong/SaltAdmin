from flask import Flask

import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/index')
def index():
    return 'this is index!'

if __name__ == '__main__':
    app.run()
