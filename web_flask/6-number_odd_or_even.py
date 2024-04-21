#!/usr/bin/python3
"""Starts a web application listening on
0.0.0.0 port 5000
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Returns 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def fun(text):
    """Returns a text"""
    return "c {}".format(text.replace('_', ' '))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pyth(text="is cool"):
    """Returns a text"""
    return "python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def num(n):
    """Returns <n> is a number only if it is a number"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(nte=None):
    """Returns an html page if n is an integer"""
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n=None):
    """Returns odd or even number"""
    if isinstance(n, int):
        if n % 2 == 0:
            res = "even"
        else:
            res = "odd"
        return render_template("6-number_odd_or_even.html", n=n, res=res)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
