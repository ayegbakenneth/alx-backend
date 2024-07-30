#!/usr/bin/env python3
""" File executable path """

from flask import Flask, request, render_template
from flask_babel import Babel
""" Module importation path """


app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Configuration class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

@babel.localeselector
def get_locale():
    """ Method to determine the best match
    with our supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route("/")
def home():
    """ A method that return the home page. """
    return render_template('2-index.html')

if __name__ = ('__main__'):
    app.run(debug=True)
