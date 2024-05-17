#!/usr/bin/python3
"""HBNB Module to use 3 routes
/         : Display Hello HBNB!
/hbnb     : Display HBNB
/c/<text> : Display C following by the value of text"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    """route to display Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """route to display hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """route to display C followed by text"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


if __name__ == "__main__":
    """Main function"""
    app.run(host="0.0.0.0", port=5000)
