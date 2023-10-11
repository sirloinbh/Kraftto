from flask import Flask, request, render_template, Blueprint
from pymongo import MongoClient
from modules.ramdom_manito import krafton_paticipants, user_datas

client = MongoClient('localhost', 27017)
db = client.kraftto

mission_complete_bp = Blueprint('mission_complete', __name__)


@mission_complete_bp.route('/mission/complete', methods=['GET', 'POST'])
def weekly_mission_complete():
    # 미션 완료 페이지 렌더링
    # DB에서 자신의 마니또의 힌트를 가지고와서 보여줌

    if id == 4:
        render_template('final_complete.html')
    # 1~4주차 메세지 모두를 불러온다.
    return render_template('complete.html')
