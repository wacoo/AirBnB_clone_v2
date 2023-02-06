#!/usr/bin/python3
from flask import Flask
""" Start a web app that listens to
any ip and port 5000. Prints Hello HBNB! at /
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
