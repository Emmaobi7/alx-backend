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
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
supported_locale = ['en', 'fr']


@babel.localeselector
def get_locale():
    """
    guess best language
    """
    user_locale = request.args.get('locale')
    if user_locale and user_locale in supported_locale:
        return user_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    simple web page
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
