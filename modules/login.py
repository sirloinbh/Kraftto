import hashlib
import datetime

import jwt
from flask import Flask, request, render_template, Blueprint, redirect, url_for, jsonify
from pymongo import MongoClient

SECRET_KEY = 'secrete key'

client = MongoClient('localhost', 27017)
db = client.kraftto

login_bp = Blueprint('login', __name__)


@login_bp.route('/login', methods=['GET'])
def login_func():
    return render_template('login.html')


@login_bp.route('/login', methods=['POST'])
def login_api():
    email = request.form['email']
    password = request.form['password']

    hashed_pw = hashlib.sha256(password.encode('utf-8')).hexdigest()

    find_user = db.user.find_one({'email': email, 'password': hashed_pw})
    print(find_user)

    if find_user:
        payload = {
            'email': email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60 * 60 * 1)
        }
        if find_user['email'] == 'admin':
            return redirect(url_for('admin.admin_func'))

        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return jsonify({'result': 'success', 'token': token})
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})
