from flask import Flask

from models import db
from login_form import LoginForm
from flask import render_template

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route("/")
    def login_form():
        title = "Log in"
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)
    return app

if __name__ == '__main__':
    create_app()