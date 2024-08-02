#!/usr/bin/env python3
""" File executable path """

from flask import Flask, g, render_template, request
""" Module importation path """

app = Flask(__name)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """ Method to get user info """
    return users.get(user_id)


def get_locale():
    """ A method to get user prefered locale """
    supported_locales = ['en', 'fr', 'kg']
    user_locale = None

    user_id = int(request.args.get('login_as', 0))
    if user_id in users:
        user_locale = users[user_id].get('locale')
    if not user_locale and g.user:
        user_locale = g.user.get('locale')

    if not user_locale:
        user_locale = request.headers.get(
                'Accept-Language', '').split(',')[0][:2]

    if user_locale not in supported_locales:
        user_locale = 'en'

    return user_locale


@app.before_request
def before_request():
    """ To add to the global variable """
    user_id = int(request.args.get('login_as', 0))
    g.user = get_user(user_id)
    g.locale = get_locale()


@app.route('/')
def index():
    """ The home route """
    message = "You are not logged in."
    if g.user:
        message = f"You are logged in as {g.user['name']}."

    return render_template('6-index.html', message=message, locale=g.locale)


if __name__ == '__main__':
    app.run()
