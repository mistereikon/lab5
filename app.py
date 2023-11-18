# app.py

from flask import Flask, render_template, flash, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
csrf = CSRFProtect(app)

class LoginForm(FlaskForm):
    username = StringField('Ім\'я користувача', validators=[DataRequired(message='Це поле обов\'язкове')])
    password = PasswordField('Пароль', validators=[DataRequired(message='Це поле обов\'язкове'), Length(min=4, max=10)])
    remember = BooleanField('Запам\'ятати мене')

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if form.username.data == 'admin' and form.password.data == 'password':
            session['username'] = form.username.data
            flash('Успішний вхід!', 'success')
            return redirect(url_for('info'))
        else:
            flash('Невірне ім\'я користувача або пароль', 'danger')

    return render_template('login.html', form=form)

@app.route('/info')
def info():
    return render_template('info.html')

if __name__ == '__main__':
    app.run(debug=True)
