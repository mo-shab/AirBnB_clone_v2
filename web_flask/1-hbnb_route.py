#!/usr/bin/python3
"""HBNB Module to use 3 routes
/         : Display Hello HBNB!
/hbnb     : Display HBNBt"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    """Function Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Second hbnb route"""
    return 'HBNB'


if __name__ == "__main__":
    """Mian function"""
    app.run(host="0.0.0.0", port=5000)
