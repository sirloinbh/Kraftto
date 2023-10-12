import jwt
from flask import Flask, request, render_template, Blueprint, redirect, url_for
from pymongo import MongoClient
from modules.userdatas import krafton_paticipants

client = MongoClient('localhost', 27017)
db = client.kraftto

mission_complete_bp = Blueprint('mission_complete', __name__)

userdata = {
    "username": "강철구"
}


@mission_complete_bp.route('/mission/complete', methods=['GET', 'POST'])
def mission_complete_fun():
    weeknumber = request.args.get('weeknumber')
    person_i_got_help = db.user.find_one({'username': userdata['username']})[
        'person_i_got_help']
    messages = list(db.message.find({'username': person_i_got_help}))
    hint = db.user.find_one({'username': person_i_got_help})
    print(hint["OS"])

    return render_template("complete.html", weeknumber=weeknumber, messages=messages)


@mission_complete_bp.route('/mission/final_complete', methods=['GET', 'POST'])
def mission_final_complete_fun():
    weeknumber = request.args.get('weeknumber')
    user = db.user.find_one({'username': userdata['username']})
    person_i_got_help = db.user.find_one({'username': userdata['username']})[
        'person_i_got_help']

    messages = list(db.message.find({'username': person_i_got_help}))
    print(messages)
    return render_template("final_complete.html", weeknumber=weeknumber, messages=messages, person_i_got_help=person_i_got_help, user=user)
