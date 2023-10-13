import jwt
from flask import Flask, request, render_template, Blueprint, redirect, url_for
from pymongo import MongoClient

from modules.login import SECRET_KEY
from modules.userdatas import krafton_paticipants
import random
from bson import ObjectId

client = MongoClient('mongodb://sun:shine@13.209.47.134', 27017)
db = client.kraftto
admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/admin', methods=['GET', 'POST'])
def admin_func():
    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user = db.user.find_one({"email": payload["email"]})

        not_approved_message = list(db.message.find({'is_approved': False}))
        print(not_approved_message)
        return render_template('admin.html', user=user, messages=not_approved_message)

    except jwt.ExpiredSignatureError:
        return redirect(url_for("login.login_api", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login.login_api", msg="로그인 정보가 존재하지 않습니다."))


@admin_bp.route('/admin/update', methods=['GET', 'POST'])
def admin_approve():
    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user = db.user.find_one({"email": payload["email"]})

        _id = request.args.get('_id')
        obj_id = ObjectId(_id)

        # Use the correct query condition to find the document by its ObjectId
        db.message.update_one({"_id": obj_id}, {'$set': {'is_approved': True}})
        print(db.message.find_one({"_id": obj_id})['username'])

        db.user.update_one(
            {"username": db.message.find_one({"_id": obj_id})['username']}, {'$set': {'current_mission': ''}})

        not_approved_message = list(db.message.find({'is_approved': False}))

        return render_template('admin.html', user=user, messages=not_approved_message)

    except jwt.ExpiredSignatureError:
        return redirect(url_for("login.login_api", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login.login_api", msg="로그인 정보가 존재하지 않습니다."))
