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

userdata = {
    'username': "강철구"
}


@mission_bp.route('/mission', methods=['GET', 'POST'])
def mission_func():
    token_receive = request.cookies.get('mytoken')
    weeknumber = request.args.get("weeknumber")

    try:
        if request.method == "POST":
            message = {
                'username': userdata['username'],
                f"message{weeknumber}": request.form.get("message"),
                "is_approved": False,
            }
            db.message.insert_one(message)
            print("생성")
            return redirect(url_for('main.main_func'))

        user_data = db.user.find_one({'username': userdata['username']})

        if user_data['current_mission'] == "":
            user_data['current_mission'] = random.choice(
                list(db.mission.find()))['description']
            db.user.update_one(
                {'username': userdata['username']},
                {"$set": {'current_mission': user_data['current_mission']}}
            )

        random_mission = user_data['current_mission']

        return render_template('mission.html', weeknumber=weeknumber, random_mission=random_mission)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))
