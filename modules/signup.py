import hashlib

from flask import Flask, request, render_template, Blueprint, redirect, url_for
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.kraftto
signup_bp = Blueprint('signup', __name__)


@signup_bp.route('/signup', methods=['GET'])
def signup_func():
    return render_template('signup.html')


@signup_bp.route('/signup', methods=['POST'])
def signup_api():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    OS = request.form['OS']
    gender = request.form['gender']
    junglenumber = request.form['junglenumber']

    hashed_pw = hashlib.sha256(password.encode('utf-8')).hexdigest()

    new_user = {
        'username': username,
        'email': email,
        'password': hashed_pw,
        'OS': OS,
        'gender': gender,
        'junglenumber': junglenumber,
        "is_manitto": False,
        "person_i_help": "",
        "person_i_got_help": "",
        "message1": "",
        "message2": "",
        "message3": "",
        "message4": "",
    }

    db.user.insert_one(new_user)

    return render_template('login.html')