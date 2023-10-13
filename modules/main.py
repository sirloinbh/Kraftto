import jwt
from flask import Flask, request, render_template, Blueprint, redirect, url_for, jsonify
from pymongo import MongoClient

from modules.login import SECRET_KEY
from modules.userdatas import krafton_paticipants
import random


client = MongoClient('mongodb://sun:shine@13.209.47.134', 27017)
db = client.kraftto
main_bp = Blueprint('main', __name__)


@main_bp.route('/main', methods=['GET'])
def main_func():
    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user = db.user.find_one({"email": payload["email"]})
        krafton_paticipants = list(db.paticipants.find())

        week1_approved = False
        week2_approved = False
        week3_approved = False
        week4_approved = False

        if user['is_manitto'] == False:
            print("마니또가 아직 없습니다. 룰렛을 돌려주세요.")
            return render_template('main.html', user=user, participants=krafton_paticipants)

        if user['person_i_got_help'] == "":
            user_lists = list(db.user.find())
            for users in user_lists:
                if users['person_i_help'] == user['username']:
                    db.user.update_one({"username": user['username']}, {
                        "$set": {'person_i_got_help': users['username']}})

        if user:
            week1_approved = bool(db.message.find_one(
                {"username": user['username'], 'message1': {'$exists': True}, 'is_approved': True}))
            week2_approved = bool(db.message.find_one(
                {"username": user['username'], 'message2': {'$exists': True}, 'is_approved': True}))
            week3_approved = bool(db.message.find_one(
                {"username": user['username'], 'message3': {'$exists': True}, 'is_approved': True}))
            week4_approved = bool(db.message.find_one(
                {"username": user['username'], 'message4': {'$exists': True}, 'is_approved': True}))

        return render_template('main.html', user=user, week1_approved=week1_approved, week2_approved=week2_approved, week3_approved=week3_approved, week4_approved=week4_approved)

    except jwt.ExpiredSignatureError:
        return redirect(url_for("login.login_func", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login.login_func", msg="로그인 정보가 존재하지 않습니다."))


@main_bp.route('/main', methods=['POST'])
def roulette_func():
    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user = db.user.find_one({"email": payload["email"]})
        db.user.update_one({'username': user['username']}, {
                           '$set': {'is_manitto': True}})
        db.user.update_one({'username': user['username']}, {
                           '$set': {'person_i_help': request.form.get('selectedperson').split('.')[1]}})
        db.paticipants.delete_one(
            {'username': request.form.get('selectedperson')})

        return render_template('main.html', user=user)

    except jwt.ExpiredSignatureError:
        return redirect(url_for("login.login_func", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login.login_func", msg="로그인 정보가 존재하지 않습니다."))
