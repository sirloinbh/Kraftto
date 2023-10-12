import jwt
from flask import Flask, request, render_template, Blueprint, redirect, url_for
from pymongo import MongoClient
from modules.userdatas import krafton_paticipants

client = MongoClient('localhost', 27017)
db = client.kraftto

mission_complete_bp = Blueprint('mission_complete', __name__)


@mission_complete_bp.route('/mission/complete', methods=['GET', 'POST'])
def mission_complete_fun():
    token_receive = request.cookies.get('mytoken')

    try:
        return render_template('final_complete.html')
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))
