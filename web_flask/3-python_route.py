#!/usr/bin/python3
"""
Write a script that starts a Flask web application
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """index"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cis_fun(text):
    """cis_fun"""
    s = text
    s = s.replace("_", " ")
    return "C {}".format(s)


@app.route("/python", strict_slashes=False)
def py():
    """cis_fun"""
    return "Python is cool"


@app.route("/python/<text>", strict_slashes=False)
def py1(text):
    """cis_fun"""
    s = text
    s = s.replace("_", " ")
    return "Python {}".format(s)


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
