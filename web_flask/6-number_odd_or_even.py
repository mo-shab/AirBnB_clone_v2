#!/usr/bin/python3
"""HBNB Module to use 3 routes
/                       : Display Hello HBNB!
/hbnb                   : Display HBNB
/c/<text>               : Display C following by the value of text
/python/<text>          : Display python follwoing by the value of text.
                          default value of text is 'is cool'
/number/<n>             : Display 'n' is a number only if 'n' is int
/number_template/<n>    : Display HTML page only if n is int
/number_odd_or_even/<n> : display a HTML page only if n is an integer:
                          tag: “Number: n is even|odd” inside the tag BODY"""


from flask import Flask, render_template


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
    return "c {}".format(text)


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """route to display python followed by test.
       the default value of text is 'is cool'"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """route to display 'n' is a number only if 'n' is int"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """route to display HTML page only if n is int"""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_even(n):
    """route to display HTML page only if n is int
       Number: n is even|odd"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    """Main function"""
    app.run(host="0.0.0.0", port=5000)
