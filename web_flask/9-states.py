#!/usr/bin/python3
"""
    Module that List states and cities
"""


from flask import Flask, render_template
from models import *
from models import storage


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """Function that display a list of states"""
    states = storage.all('State').values()
    return render_template('9-states.html', states=states, condition="states_list")


@app.route('/states/<id>', strict_slashes=False)
def states_list_id(id):
    """Function that display a list of states"""
    states = storage.all('State').values()
    print(states)
    try:
        state_id = states[id]
        return render_template(
            '9-states.html',
            state_id=state_id,
            condition="state_id")
    except:
        return render_template('9-states.html', condition="not_found")


@app.teardown_appcontext
def teardown_db(exception):
    """Close the storage on reardown after each request"""
    storage.close()


if __name__ == "__main__":
    """Main function"""
    app.run(host="0.0.0.0", port=5000)
