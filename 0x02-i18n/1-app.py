#!/usr/bin/env python3
"""
a basic flask app
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

class Config():
    """
    babel language config class
    """
    LANGUAGES = ["en", "fr"]

app.config.from_object(Config)


@app.route('/')
def index():
    """
    simple web page
    """
    return render_template('1-index.html')

if __name__ == '__main__':
    app.run()