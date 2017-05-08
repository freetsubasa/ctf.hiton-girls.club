#!/usr/bin/python2.7
from flask import Flask, request, flash, render_template, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
import requests, sys

app = Flask(__name__)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(255), unique = True, nullable = False)
    username = db.Column(db.String(255), unique = True, nullable=False)
    encrypted_password = db.Column(db.String(255), unique = True, nullable=False)
    point = db.Column(db.Integer)

@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))

@app.route('/')
@app.route('/index')
def hello_world():
  return render_template('index.html')

@app.route('/problems')
def list_problems():
    return render_template('problems.html')

@app.route('/rank')
def rank():
    return render_template('rank.html')

@app.route('/lecture')
def lecture():
    return render_template('lecture.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    return render_template('register.html')

@app.route('/forgot_password')
def reset_password():
    return render_template('forgot_password.html')

@app.route('/user/<name>')
def get_user_name(name):
    return render_template('user.html', name =name)

@app.route('/login', methods = ["GET", "POST"])
def login():
    error = None
    if request.method == 'POST':
        user = User.query.filter_by(username = request.form['username']).first()
        password = request.form['password']
        if user is None:
            error = 'Invalid Username'
        elif password != user.encrypted_password:
            error = 'Invalid Password'
        else:
            login_user(user)
            return redirect(url_for('list_problems'))
    return render_template('login.html', error = error)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('hello_world'))

if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0')
