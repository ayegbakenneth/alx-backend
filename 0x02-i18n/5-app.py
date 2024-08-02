#!/usr/bin/env python3
""" File executable path """

from flask import Flask, g, render_template, request
""" Module importation path """

app = Flask(__name__)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user(user_id):
    """ A method that get a user info """
    return users.get(user_id)

@app.before_request
def before_request():
    """" Do this before other method """
    user_id = int(request.args.get('login_as', 0))
    g.user = get_user(user_id)

@app.route('/')
def index():
    """ Home route """
    message = None
    if g.user:
        if g.user['locale'] == 'fr':
            message = f"Vous êtes connecté en tant que {g.user['name']}."
        else:
            message = f"You are logged in as {g.user['name']}."
    else:
        if g.user and g.user['locale'] == 'fr':
            message = "Vous n'êtes pas connecté."
        else:
            message = "You are not logged in."

    return render_template('5-index.html', message=message)

if __name__ == '__main__':
    app.run()
