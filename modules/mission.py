import random
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from ramdom_manito import krafton_paticipants, user_datas
from mission_data import weekly_missions
app = Flask(__name__)


@app.route('/main', methods=['GET', 'POST'])
def get_user_data():
    # 랜덤으로 지정된 자신의 마니또 데이터를 불러오기.
    userdata = user_datas[0]
    return render_template('main.html', userdata=userdata)


@app.route('/mission', methods=['GET', 'POST'])
def weekly_mission():
    weeknumber = request.args.get("weeknumber")
    random_mission = weekly_missions['mission1']

    if request.method == "POST":
        message = request.form.get("message")
        print(message)
        # POST = Message -> DB 전달
        return redirect(url_for("get_user_data"))

    return render_template('mission.html', weeknumber=weeknumber, random_mission=random_mission)
    return render_template('mission.html')
  
@app.route('/mission/complete', methods=['GET', 'POST'])
def weekly_mission_complete():
    # 미션 완료 페이지 렌더링
    # DB에서 자신의 마니또의 힌트를 가지고와서 보여줌

    if id == 4:
        render_template('final_complete.html')
    # 1~4주차 메세지 모두를 불러온다.
    return render_template('complete.html')


if __name__ == '__main__':
    app.run(debug=True)
