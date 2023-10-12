
from flask import Flask, request, render_template, Blueprint, redirect, url_for
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.kraftto
signup_bp = Blueprint('signup', __name__)


@signup_bp.route('/signup', methods=['GET', 'POST'])
def signup_func():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        doc = {
            'username': username,
            'password': password
        }

        db.user.insert_one(doc)

        return redirect(url_for('login.login'))
    else:
        return render_template('signup.html')
