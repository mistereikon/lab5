# forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Ім\'я користувача', validators=[DataRequired(message='Це поле обов\'язкове')])
    password = PasswordField('Пароль', validators=[DataRequired(message='Це поле обов\'язкове'), Length(min=4, max=10)])
    remember = BooleanField('Запам\'ятати мене')
