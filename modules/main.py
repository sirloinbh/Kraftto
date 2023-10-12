from flask import Flask, request, render_template, Blueprint
from pymongo import MongoClient
from modules.userdatas import krafton_paticipants
import random


client = MongoClient('localhost', 27017)
db = client.kraftto

person_i_help = random.choice(krafton_paticipants).split('.')


main_bp = Blueprint('main', __name__)


@main_bp.route('/main', methods=['GET', 'POST'])
def main_func():
    user = db.user.find_one({"username": "마찬옥"})
    if user['is_manitto'] == False:
        print("마니또가 아직 없습니다. 룰렛을 돌려주세요.")
        user = None
        return render_template('main.html', user=user)

    return render_template('main.html', user=user)


@main_bp.route('/main/roulette', methods=['GET', 'POST'])
def roulette_func():
    # 랜덤으로 도와줄 사람 배정
    db.user.update_one({"username": "마찬옥"}, {"$set": {'is_manitto': True}})
    db.user.update_one({"username": "마찬옥"}, {
                       "$set": {'person_i_help': person_i_help[1]}})
    print(person_i_help)
    db.user.update_one({"username": person_i_help[1]}, {"$set": {'is_manitto': True}})

    user = db.user.find_one({"username": "마찬옥"})
    return render_template('main.html', user=user)


# 내가 도울 사람이 있는지 없는 지 확인 ( is_manitto )
# ( if 있다면, userdata에 있는 정보들을 불러와 보여준다.
# ( else 없다면, 룰렛을 보여준다.
#   -> 프론트엔드에 전체 참가자 리스트를 보내준다. )
#   -> 랜덤으로 지정된 참가자 데이터를 받는다. )
#   -> 참가자를 데이터베이스에 저장하고, is_manitto 값을 True로 변경한다.
