#!/usr/bin/env python3
"""Setting up a  python flask environent"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config:
    '''
    Setting up the configuration default values
    '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "fr"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    '''
    Getting the locale language using the babel.localeselector deco
    '''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', )
def index():
    """ The index page to be rendered """
    return render_template('3-index.html')
