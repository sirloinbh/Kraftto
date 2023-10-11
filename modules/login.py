from flask import Flask, request, render_template, Blueprint
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.kraftto

login_bp = Blueprint('login', __name__)


@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        find_user = db.user.find_one({'username': username})

        try:
            if find_user['password'] == password:
                # session["logged_in"] = True
                print('성공')
                return render_template('index.html')
            else:
                return '아이디 또는 비밀번호가 틀립니다.'
        except:
            return '로그인 오류'
    else:
        return render_template('login.html')
