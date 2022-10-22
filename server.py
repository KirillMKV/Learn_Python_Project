from flask import Flask

from Flask.login_form import LoginForm
from flask import render_template


app = Flask(__name__)
app.config.from_pyfile('config.py')

@app.route("/")
def login_form():
    title = "Log in"
    login_form = LoginForm()
    return render_template('login.html', page_title=title, form=login_form)


if __name__ == '__main__':
    app.run()