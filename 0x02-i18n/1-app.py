#!/usr/bin/env python3
""" File executable path """

from flask import Flask, render_template
from flask_babel import Babel
""" Module importation path """

app = Flask(__name__)
babel = Babel(app)

class Config:
    """ A class for the app config """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

@app.route("/")
def home():
    """ A method that render the home page """
    return render_template('1-index.html')

if __name__ = ('__main__'):
    app.run(debug=True)
