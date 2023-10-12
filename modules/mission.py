import random

import jwt
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, Blueprint
from modules.userdatas import krafton_paticipants
from pymongo import MongoClient

app = Flask(__name__)

mission_bp = Blueprint('mission', __name__)

client = MongoClient('localhost', 27017)
db = client.kraftto
random_int = random.randint(1, 16)


# mission_collection = db["mission"]
# mission_lists = [doc['mission'] for doc in mission_collection.find()]
# print(mission_lists)


@mission_bp.route('/mission', methods=['GET', 'POST'])
def mission_func():
    token_receive = request.cookies.get('mytoken')

    weeknumber = request.args.get("weeknumber")

    try:
        if request.method == "POST":
            message = {f"message{weeknumber}": request.form.get("message")}
            print(message)
            db.user.update_one({'username': '마찬옥'}, {
                '$set': {f"message{weeknumber}": request.form.get("message")}})

            if weeknumber == '4':
                return redirect(url_for("mission_complete.mission_complete_fun"))
            else:
                return redirect(url_for("main.main_func"))

        random_mission = random.choice(list(db.mission.find()))['description']
        print(random_mission)

        return render_template('mission.html', user=None, weeknumber=weeknumber, random_mission=random_mission)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))
