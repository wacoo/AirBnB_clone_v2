#!/usr/bin/python3
"""
start a web app that listens to
any ip and port 5000. Prints:
Hello HBNB! at /,
HBNB at /hbnb
value of text at /c/<text>
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Display Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def show_value(text):
    """Display variable value"""
    txt = text.replace('_', ' ')
    return 'C ' + txt


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
