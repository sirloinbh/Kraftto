import random
import jwt
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, Blueprint

from modules.login import SECRET_KEY
from modules.userdatas import krafton_paticipants
from pymongo import MongoClient

app = Flask(__name__)

mission_bp = Blueprint('mission', __name__)

client = MongoClient('mongodb://sun:shine@13.209.47.134', 27017)
db = client.kraftto
random_int = random.randint(1, 16)


@mission_bp.route('/mission', methods=['GET', 'POST'])
def mission_func():
    token_receive = request.cookies.get('mytoken')
    weeknumber = request.args.get("weeknumber")

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user = db.user.find_one({"email": payload["email"]})

        if request.method == "POST":
            message = {
                'username': user['username'],
                f"message{weeknumber}": request.form.get("message"),
                "is_approved": False,
            }
            db.message.insert_one(message)
            return redirect(url_for('main.main_func'))

        missions_lists = list(db.mission.find())
        random_missions = [mission['description']
                           for mission in missions_lists]
        print(random_missions)

        return render_template('mission.html', user=user, weeknumber=weeknumber, random_missions=random_missions)

    except jwt.ExpiredSignatureError:
        return redirect(url_for("login.login_api", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login.login_api", msg="로그인 정보가 존재하지 않습니다."))


@mission_bp.route('/mission/rullet', methods=['POST', "GET"])
def mission_rullet_func():
    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user = db.user.find_one({"email": payload["email"]})

        db.user.update_one({'username': user['username']}, {
                           '$set': {'current_mission': request.form.get('selectedmission')}})

        return render_template('mission.html', user=user)

    except jwt.ExpiredSignatureError:
        return redirect(url_for("login.login_func", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login.login_func", msg="로그인 정보가 존재하지 않습니다."))
