from flask import Flask, render_template, request, session
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'secret key'

client = MongoClient('localhost', 27017)
db = client.kraftto


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']

        find_user = db.user.find_one({'name': name})


        try:
            if find_user['password'] == password:
                session["logged_in"] = True
                return render_template('mission.html')
            else:
                return '아이디 또는 비밀번호가 틀립니다.'
        except:
            return '로그인 오류'
    else:
        return render_template('login.html')
