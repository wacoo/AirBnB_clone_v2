#!/usr/bin/python3
<<<<<<< HEAD
"""the `2-c_route` module
starts a flask web application listening on `0.0.0.0:5000`
"""
from flask import Flask, escape

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    """returns `Hello HBNB!` message"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns `HBNB` message"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """returns `c` + `text`"""
    text = text.replace("_", " ")
    return "C %s" % escape(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
=======
"""
starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """display “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
>>>>>>> 212529db4b955a72d996660137790c2497399ff5
