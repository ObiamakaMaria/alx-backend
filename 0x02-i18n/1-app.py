#!/usr/bin/env python3
"""setting up a python flask environent"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


class Config:
    '''
    Setting up configuration default values
    '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', )
def index():
    """The index page to be rendered"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(port=5000)
