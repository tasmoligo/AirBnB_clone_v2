#!/usr/bin/python3
"""Starts a web application listening on
0.0.0.0 port 5000
"""

from flask import Flask

app = Flask("__name__")


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
    return "C {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
