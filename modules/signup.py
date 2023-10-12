
from flask import Flask, request, render_template, Blueprint, redirect, url_for
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.kraftto
signup_bp = Blueprint('signup', __name__)


@signup_bp.route('/signup', methods=['GET', 'POST'])
def signup_func():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        OS = request.form['OS']
        gender = request.form['gender']
        junglenumber = request.form['junglenumber']

        new_user = {
            'username': username,
            'email': email,
            'password': password,
            'OS': OS,
            'gender': gender,
            'junglenumber': junglenumber,
        }

        db.user.insert_one(new_user)

        return redirect(url_for('login.login'))
    else:
        return render_template('signup.html')
