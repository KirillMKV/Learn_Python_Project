from flask import Flask
from flask_login import LoginManager, login_user, logout_user

from models import db, User
from login_form import LoginForm
from flask import render_template, flash, redirect, url_for

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route("/login")
    def login_form():
        title = "Log in"
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)

    @app.route('/process-login', methods=['POST'])
    def process_login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                flash('Access is allowed')
                return redirect(url_for('start_page'))
        flash('Incorrect username or password')
        return redirect(url_for('login'))

    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('start_page'))

    return app

if __name__ == '__main__':
    create_app()