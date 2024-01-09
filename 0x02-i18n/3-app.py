#!/usr/bin/env python3
"""
a basic flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

class Config():
    """
    babel language config class
    """
    LANGUAGES = ["en", "fr"]

app.config.from_object(Config)

@babel.localeselector
def get_locale():
    """
    guess best language
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])



@app.route('/')
def index():
    """
    simple web page
    """
    return render_template('3-index.html')

if __name__ == '__main__':
    app.run()
