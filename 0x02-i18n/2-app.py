#!/usr/bin/env python3
""" Get locale from request """
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """ config class"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ get locale"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index():
    """ index """
    return render_template("2-index.html")
