#!/usr/bin/python3
""" Start a web app that listens to
any ip and port 5000. Prints Hello HBNB! at / and
HBNB at /hbnb
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

if __name__ == "__main__":
    app.runt(host="0.0.0.0", port="5000")
