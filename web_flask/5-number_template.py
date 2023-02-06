#!/usr/bin/python3
"""
start a web app that listens to
any ip and port 5000. Prints:
Hello HBNB! at /,
HBNB at /hbnb
value of text at /c/<text>
"""
from flask import Flask, escape, render_template


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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """display “Python ”, followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n='is cool'):
    """
    Check if n is a number and display
    'n is a number' i it is"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_temp(n):
    """display n inside an h1 tag
    if it is a number"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
