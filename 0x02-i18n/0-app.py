#!/usr/bin/env python3
"""Setting up a python flask environent"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', )
def index():
    """The index page to be rendered"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(port=5000)
