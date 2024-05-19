#!/usr/bin/python3
"""
    Module that List states and cities
"""


from flask import Flask, render_template
from models import *
from models import storage


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters_list():
    """
        method to display html page 6-index.html
    """
    states = storage.all('State').values()
    amenities = storage.all('Amenity').values()
    return render_template(
        "10-hbnb_filters.html",
        states=states, amenities=amenities)


def handle_teardown(self):
    """
        method to handle teardown
    """
    storage.close()



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
