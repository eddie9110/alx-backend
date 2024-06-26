#!/usr/bin/env python3

"""
flask app
"""

from flask import Flask, g, render_template, request
from flask_babel import Babel
from typing import Dict


class Config:
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    """selects best language based on the locale"""
    locale = request.args.get("locale")
    if locale and locale in app.config["LANGUAGES"]:
        return locale
    elif g.user:
        locale_ = g.user.get("locale")
        if locale_ in app.config["LANGUAGES"]:
            return locale_
    else:
        return request.accept_languages.best_match(app.config["LANGUAGES"])

def get_user():
    """returns a user dictionary or None if the ID
    cannot be found or if login_as was not passed"""
    id_ = request.args.get("login_as")
    if id_ and id_ in users.keys():
        return users.get(id)
    return None

@app.before_request
def before_request():
    """ finds a user, and sets them as a global on flask.g.user"""
    g.user = get_user()

@babel.timezoneselector
def get_timezone():
    """Determines appropriate timezone for a web page"""
    user_timezone = request.args.get('timezone')
    if user_timezone:
        return user_timezone
    user_ = get_user()
    if user_ and user_['timezone']:
        return user_['timezone']
    return Config.BABEL_DEFAULT_TIMEZONE

@app.route("/")
def hello():
    """root route"""
    return render_template("6-index.html", user=g.user)


if __name__ == "__main__":
    app.run()                                                                                     1,20   
