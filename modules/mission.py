import random
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, Blueprint
from modules.ramdom_manito import krafton_paticipants, user_datas
from modules.mission_data import weekly_missions


app = Flask(__name__)

mission_bp = Blueprint('mission', __name__)


@mission_bp.route('/mission', methods=['GET', 'POST'])
def weekly_mission():
    weeknumber = request.args.get("weeknumber")
    random_mission = weekly_missions['mission1']

    if request.method == "POST":
        message = request.form.get("message")
        print(message)
        # POST = Message -> DB 전달
        return redirect(url_for("get_user_data"))

    return render_template('mission.html', weeknumber=weeknumber, random_mission=random_mission)


if __name__ == '__main__':
    app.run(debug=True)
