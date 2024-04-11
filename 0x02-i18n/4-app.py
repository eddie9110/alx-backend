#!/usr/bin/env python3

"""
flask app
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """selects best language based on the locale"""
    locale = request.args.get("locale")
    if locale and locale in app.config["LANUAGES"]:
        return locale
    else:
        return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def hello():
    """root route"""
    return render_template("4-index.html")



if __name__ == "__main__":
    app.run()
