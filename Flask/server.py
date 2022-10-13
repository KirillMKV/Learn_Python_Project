from flask import Flask, render_template
from registration_form import RegistrationForm
from Flask.login_form import LoginForm
from DB.models import User
from DB.create_db import db_session

import datetime


app = Flask(__name__)
app.config.from_pyfile('/home/kirillmkv/PycharmProjects/Learn_Python/Learn_Python_Project/config.py')


@app.route('/')
def start_page():
    return render_template('index.html')


@app.route('/login')
def login_form():
    title = "Log in"
    login_form = LoginForm()
    return render_template('login.html', page_title=title, form=login_form)


@app.route('/registration', methods=['GET'])
def registration():
    title = "Registration"
    registration_form = RegistrationForm()
    return render_template('registration_form.html', page_title=title, form=registration_form)


@app.route('/registration_submit', methods=['POST', 'GET'])
def registration_submit():
    form = RegistrationForm()
    user = User()
    user.username = form.username.data
    user.first_name = form.first_name.data
    user.last_name = form.last_name.data
    user.email = form.email.data
    user.password = form.password.data
    user.registration_date = datetime.date.today().strftime("%y-%m-%d")
    db_session.add(user)
    db_session.commit()

if __name__=="__main__":
    app.run(debug=True)