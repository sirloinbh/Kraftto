from flask import Flask, request, render_template, Blueprint
from pymongo import MongoClient
from modules.userdatas import krafton_paticipants

client = MongoClient('localhost', 27017)
db = client.kraftto

mission_complete_bp = Blueprint('mission_complete', __name__)


@mission_complete_bp.route('/mission/complete', methods=['GET', 'POST'])
def mission_complete_fun():
    all_messages = list(db.user.find({'username': "마찬옥"}, {
        'message1': True, 'message2': True, 'message3': True, 'message4': True}))[0]
    person_i_got_help = db.user.find_one({'username': "강철구"})

    print(all_messages, person_i_got_help)

    return render_template('final_complete.html', message=all_messages, person_i_got_help=person_i_got_help)
