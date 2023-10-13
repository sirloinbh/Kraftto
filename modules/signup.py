import hashlib
import re

from flask import Flask, request, render_template, Blueprint, redirect, url_for
from pymongo import MongoClient

client = MongoClient('mongodb://sun:shine@13.209.47.134', 27017)
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

    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    password_pattern = r'^(?=.*[A-Za-z0-9])(?=.*[\W_]).{8,}$'
    check_email = True
    check_password = True
    check_password_confirm = True
    check_user_duplication = True

    find_user = db.user.find_one({"email": email})
    if find_user:
        check_user_duplication = False

    if not re.match(email_pattern, email):
        check_email = False
    if not re.match(password_pattern, password):
        check_password = False

    passwordConfirm = request.form['passwordConfirm']
    if password != passwordConfirm:
        check_password_confirm = False

    if not check_password or not check_email or not check_password_confirm or not check_user_duplication:
        return render_template('signup.html', check_password=check_password, check_email=check_email,
                               check_password_confirm=check_password_confirm, check_user_duplication=check_user_duplication)

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
        "current_mission": ""
    }

    db.user.insert_one(new_user)

    return render_template('login.html')
