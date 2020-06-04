from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField,SubmitField,BooleanField                             # for creating string field
from wtforms.validators import DataRequired, Length,Email,EqualTo         #importing validators


class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired],Email())
    password=PasswordField('Password',validators=[DataRequired])
    remember=BooleanField('Remember Me')
    submit=SubmitField('Login')

