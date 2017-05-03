#!/usr/bin/python2.7
from flask import Flask
from flask import request
from flask import render_template
import requests

app = Flask(__name__)

@app.route('/')
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

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/forgot_password')
def reset_password():
    return render_template('forgot_password.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return 'logout'


if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0')
