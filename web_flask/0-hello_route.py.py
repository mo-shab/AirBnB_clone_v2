#!/usr/bin/python3
"""Hello world! Module for Flask"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def Hello_HBNB():
    return 'Hello HBNB!'

if __name__ == '__main__':
    Hello_HBNB()