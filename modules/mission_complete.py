import jwt
from flask import Flask, request, render_template, Blueprint, redirect, url_for
from pymongo import MongoClient
from modules.userdatas import krafton_paticipants
from modules.login import SECRET_KEY

client = MongoClient('mongodb://sun:shine@13.209.47.134', 27017)
db = client.kraftto

mission_complete_bp = Blueprint('mission_complete', __name__)


@mission_complete_bp.route('/mission/complete', methods=['GET', 'POST'])
def mission_complete_fun():
    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user = db.user.find_one({"email": payload["email"]})

        weeknumber = request.args.get('weeknumber')
        person_i_got_help = db.user.find_one({'username': user['username']})[
            'person_i_got_help']
        print(person_i_got_help)

        messages = list(db.message.find({'username': person_i_got_help}))
        hints = db.user.find_one({'username': person_i_got_help})
        if messages == []:
            messages = None

        return render_template("complete.html", user=user, weeknumber=weeknumber, messages=messages, hints=hints)

    except jwt.ExpiredSignatureError:
        return redirect(url_for("login.login_func", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login.login_func", msg="로그인 정보가 존재하지 않습니다."))


@mission_complete_bp.route('/mission/final_complete', methods=['GET', 'POST'])
def mission_final_complete_fun():
    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user = db.user.find_one({"email": payload["email"]})

        weeknumber = request.args.get('weeknumber')
        user = db.user.find_one({'username': user['username']})
        person_i_got_help = db.user.find_one({'username': user['username']})[
            'person_i_got_help']

        messages = list(db.message.find({'username': person_i_got_help}))
        print(messages)
        return render_template("final_complete.html", weeknumber=weeknumber, messages=messages, person_i_got_help=person_i_got_help, user=user)

    except jwt.ExpiredSignatureError:
        return redirect(url_for("login.login_func", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login.login_func", msg="로그인 정보가 존재하지 않습니다."))
