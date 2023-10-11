from flask import Flask, render_template, request, session, redirect, url_for, flash, jsonify
from pymongo import MongoClient
from modules.login import login_bp

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.kraftto


@app.route('/')
def main():
    return render_template('Kraftto.html')


# login
app.register_blueprint(login_bp)


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
