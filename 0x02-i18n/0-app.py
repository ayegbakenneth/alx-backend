#!/usr/bin/env python3
""" File executable path """

from flask import Flask
from flask import render_template
""" Module import path """

app = Flask(__name__)


@app.route('/')
def home():
    """ A method that direct to the home page """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug = True)
