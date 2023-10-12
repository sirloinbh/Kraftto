import jwt
from flask import Flask, request, render_template, Blueprint, redirect, url_for
from pymongo import MongoClient

from modules.login import SECRET_KEY
from modules.userdatas import krafton_paticipants
import random


client = MongoClient('localhost', 27017)
db = client.kraftto

person_i_help = random.choice(krafton_paticipants).split('.')


main_bp = Blueprint('main', __name__)


@main_bp.route('/main', methods=['GET', 'POST'])
def main_func():
    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user = db.user.find_one({"email": payload["email"]})

        if not user['is_manitto']:
            print("마니또가 아직 없습니다. 룰렛을 돌려주세요.")
            return render_template('main.html', user=user, is_manitto=True)

        if user['person_i_got_help'] == '':
            users = list(db.user.find())
            for user in users:
                print(user.get('person_i_help'))

                if user.get('person_i_help') == '강철구':
                    db.user.update_one({"username": "강철구"}, {
                        "$set": {'person_i_got_help': "마찬옥"}})

        return render_template('main.html', user=user)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login.login_func", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login.login_func", msg="로그인 정보가 존재하지 않습니다."))



@main_bp.route('/main/roulette', methods=['GET', 'POST'])
def roulette_func():
    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user = db.user.find_one({"email": payload["email"]})

        # 랜덤으로 도와줄 사람 배정
        db.user.update_one({"username": "강철구"}, {"$set": {'is_manitto': True}})
        db.user.update_one({"username": "강철구"}, {
            "$set": {'person_i_help': person_i_help[1]}})
        print(person_i_help)
        # db.user.update_one({"username": person_i_help[1]}, {"$set": {'person_i_got_help': True}})

        user = db.user.find_one({"username": "강철구"})
        return render_template('main.html', user=user)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))


# 내가 도울 사람이 있는지 없는 지 확인 ( is_manitto )
# ( if 있다면, userdata에 있는 정보들을 불러와 보여준다.
# ( else 없다면, 룰렛을 보여준다.
#   -> 프론트엔드에 전체 참가자 리스트를 보내준다. )
#   -> 랜덤으로 지정된 참가자 데이터를 받는다. )
#   -> 참가자를 데이터베이스에 저장하고, is_manitto 값을 True로 변경한다.
