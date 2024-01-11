#!/usr/bin/env python3
"""
a basic flask app
"""
from flask import Flask, render_template, request, g
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


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    get_user: retrive user id
    return dict or none
    """
    user_id = request.args.get('login_as')
    if not user_id:
        return None
    return users.get(int(user_id))


@app.before_request
def before_request():
    """
    before_request: find user and set as global
    execute before other funtions
    """
    func = get_user()
    if func:
        g.user = func


@app.route('/')
def index():
    """
    simple web page
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
