#!/usr/bin/python3
""" Start a web app that listens to
any ip and port 5000. Prints:
- Hello HBNB! at /,
- HBNB at /hbnb
- value of text at /c/<text>
- check is n is a number /number/<n>
- display an html tag h1 if n is a number

"""
import os
os.environ["FLASK_APP"]="0-hello_route.py"
from flask import Flask

app = Flask("__name__")
#app.url_map.strict_slashes = False
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
@app.route('/number_template/<n>', strict_slashes=False)
def num_temp(n):
    """display n inside an h1 tag
    if it is a number"""
    if n.isdigit():
        return "<!DOCTYPE html><html><head><title>HBNB</title></head><body><h1>Number: {}</h1></body></html>".format(n)
    
if __name__ == "__main__":
    app.runt(host="0.0.0.0", port="5000")
