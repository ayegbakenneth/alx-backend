#!/usr/bin/env python3
""" File interpreter path """

from pytz import UTC
from flask import Flask, render_template, request
from flask_babel import Babel
""" Module importation path """


app = Flask(__name__)
babel = Babel(app)


class Config:
    """" A class config path """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = UTC


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ A method to return a default locale """
    if 'locale' in request.args:
        locale_inf = request.arg.get('locale')
        if locale_inf in app.config['LANGUAGES']:
            return locale_inf
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
    """ A method that direct a user to the home page """
    return render_template('4-index.html')
