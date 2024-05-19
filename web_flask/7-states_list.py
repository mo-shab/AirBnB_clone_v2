#!/usr/bin/python3
"""Module that List states"""


from flask import Flask, render_template
from models import *
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Function that display a list of states"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)



@app.teardown_appcontext
def teardown_db(exception):
    """Close the storage on reardown after each request"""
    storage.close()


if __name__ == "__main__":
    """Main function"""
    app.run(host="0.0.0.0", port=5000)
