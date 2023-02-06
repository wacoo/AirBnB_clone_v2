#!/usr/bin/python3
import os
from flask import Flask
""" Start a web app that listens to
any ip and port 5000. Prints Hello HBNB! at /
"""

app = Flask("__name__")
app.url_map.strict_slashes = False
@app.route('/', strict_slashes=False)
def hello():
    """Display Hello HBNB!"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
