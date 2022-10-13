from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
import email_validator


class RegistrationForm(FlaskForm):
    username = StringField('Input Username:', validators=[DataRequired()], render_kw={"class": "form-control", "value":"test"})
    first_name = StringField('Input First Name:', validators=[DataRequired()], render_kw={"class": "form-control", "value":"test"})
    last_name = StringField('Input Last Name:', validators=[DataRequired()], render_kw={"class": "form-control", "value":"test"})
    email = StringField('Input email:', validators=[DataRequired(), Email()], render_kw={"class": "form-control", "value":"test@test.com"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"class": "form-control", "value": "test"})
    registration = SubmitField('Submit', render_kw={"class": "btn btn-success"})

