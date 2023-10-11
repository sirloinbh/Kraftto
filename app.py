from flask import Flask, render_template, request, session, redirect, url_for, flash, jsonify
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.kraftto

@app.route('/login', methods=['GET', 'POST'])
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

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        doc = {
            'username': username,
            'password': password
        }

        db.user.insert_one(doc)

        return redirect(url_for('login'))
    else:
        return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
