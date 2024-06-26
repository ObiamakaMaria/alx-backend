#!/usr/bin/env python3
"""Setting up a  python flask environent.
"""
from flask_babel import Babel
from flask import Flask, render_template, request, g


class Config:
    """Setting up the configuration default values.
    """
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


def get_user(login_id):
    """
    Returns a user dictionary or None
    """
    if login_id is None:
        return None
    return users.get(int(login_id))


@app.before_request
def before_request():
    """This func executes before others"""
    g.user = get_user(request.args.get('login_as'))


@babel.localeselector
def get_locale():
    """Getting the locale language using the babel.localeselector deco"""
    locale = request.args.get('locale')
    """
    determines if the incoming request contains locale argument
    """
    if locale:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def hello_world():
    """The index page to be rendered """
    return render_template("5-index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
