#!/usr/bin/python3
"""
Start a web app that listens to
any ip and port 5000. Prints:
- Hello HBNB! at /,
- HBNB at /hbnb
- value of text at /c/<text>
"""


from flask import Flask

app = Flask(__name__)
@app.route('/', strict_slashes=False)
def hello():
    """Display Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def show_value(text):
    """Display variable value"""
    txt = text.replace('_', ' ')
    return "C " + txt


@app.route('/python/(<text>)', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def show_vlaue_python(text="is cool"):
    """Display variable value"""
    txt = text.replace('_', ' ')
    return "Python " + txt


@app.route('/number/<n>', strict_slashes=False)
def number(n="is cool"):
    """ Check if n is a number and display
    'n is a number' i it is"""
    if n.isdigit():
        return "{} is a number".format(n)


if __name__ == "__main__":
    app.runt(host="0.0.0.0", port="5000")
