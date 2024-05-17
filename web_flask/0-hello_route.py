#!/usr/bin/python3
"""HBNB Module to use 3 routes
/         : Display Hello HBNB!"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    """Function Hello HBNB"""
    return 'Hello HBNB!'


if __name__ == "__main__":
    """Main Function to run the app"""
    app.run(host="0.0.0.0", port=5000)
