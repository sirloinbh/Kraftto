from flask import Flask, render_template, request, session, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'secret key'
userinfo = {'Mario': 'qwer1234'}

client = MongoClient('localhost', 27017)
db = client.kraftto


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        userinfo[name] = password

        doc = {
            'name': name,
            'password': password
        }

        db.user.insert_one(doc)

        return redirect(url_for('login'))
    else:
        return render_template('signup.html')
