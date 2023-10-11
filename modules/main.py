from flask import Flask, request, render_template, Blueprint
from pymongo import MongoClient
from modules.ramdom_manito import krafton_paticipants, user_datas

client = MongoClient('localhost', 27017)
db = client.kraftto

main_bp = Blueprint('main', __name__)


@main_bp.route('/main', methods=['GET', 'POST'])
def get_user_data():
    # 랜덤으로 지정된 자신의 마니또 데이터를 불러오기.
    userdata = user_datas[0]
    return render_template('main.html', userdata=userdata)
