import datetime
import hashlib

import jwt
from flask import Flask, render_template, request, session, redirect, url_for, flash, jsonify
from pymongo import MongoClient
from modules.login import login_bp, SECRET_KEY
from modules.signup import signup_bp
from modules.main import main_bp
from modules.mission_complete import mission_complete_bp
from modules.mission import mission_bp
from modules.admin import admin_bp


app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.kraftto

# login
app.register_blueprint(login_bp)

# signup
app.register_blueprint(signup_bp)

# main
app.register_blueprint(main_bp)

# mission
app.register_blueprint(mission_bp)

# mission Complete
app.register_blueprint(mission_complete_bp)

# admin
app.register_blueprint(admin_bp)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
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
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return jsonify({'result': 'success', 'token': token})
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})


if __name__ == '__main__':
    app.run(debug=True)
