#!/usr/bin/python3
<<<<<<< HEAD
"""the `5-number_template` module
starts a flask web application listening on `0.0.0.0:5000`
"""
from flask import Flask, escape, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    """returns `Hello HBNB!` message"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """returns `HBNB` message"""
    return "HBNB"


@app.route("/c/<text>")
def c(text):
    """returns `c` + `text`"""
    text = text.replace("_", " ")
    return "C %s" % escape(text)


@app.route("/python")
def python():
    "returns `Python is cool`"
    text = "is cool"
    return "Python %s" % escape(text)


@app.route("/python/<text>")
def python_text(text):
    """returns `Python ` + `text`"""
    text = text.replace("_", " ")
    return "Python %s" % escape(text)


@app.route("/number/<int:n>")
def number(n):
    """returns `n` + `is a number` only if `n` is an integer"""
    return "{} is a number".format(escape(n))


@app.route("/number_template/<int:n>")
def number_template(n):
    """returns `n` + `is a number` only if `n` is an integer"""
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>")
def number_odd_or_even(n):
    """returns `n` + `is even` if `n` is even
    else returns `n` + `is odd`
    """
    parity = "even" if n % 2 == 0 else "odd"
    return render_template("6-number_odd_or_even.html",
                           number=n, parity=parity)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
=======
"""
starts a Flask web application
"""

from flask import Flask, render_template
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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """display “Python ”, followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    """display “n is a number” only if n is an integer"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numbersandtemplates(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numbersandevenness(n):
    """display a HTML page only if n is an integer"""
    if n % 2 == 0:
        evenness = 'even'
    else:
        evenness = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           evenness=evenness)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
>>>>>>> 212529db4b955a72d996660137790c2497399ff5
