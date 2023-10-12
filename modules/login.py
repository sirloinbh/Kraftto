from flask import Flask, request, render_template, Blueprint, redirect, url_for
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.kraftto

login_bp = Blueprint('login', __name__)


@login_bp.route('/login', methods=['GET', 'POST'])
def login_func():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        find_user = db.user.find_one({'email': email})

        if find_user['password'] == password:
            # session["logged_in"] = True
            print('성공')
            return redirect(url_for("main.main_func"))
        else:
            return '아이디 또는 비밀번호가 틀립니다.'
    return render_template('login.html')
