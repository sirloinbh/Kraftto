import random
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, Blueprint
from modules.userdatas import krafton_paticipants
from modules.mission_data import weekly_missions


app = Flask(__name__)

mission_bp = Blueprint('mission', __name__)


@mission_bp.route('/mission', methods=['GET', 'POST'])
def mission_func():
    weeknumber = request.args.get("weeknumber")
    print(weeknumber)
    if weeknumber == '4':
        return render_template('final_complete.html', weeknumber=weeknumber)

    random_mission = weekly_missions['mission1']

    if request.method == "POST":
        message = request.form.get("message")
        print(message)
        # POST = Message -> DB 전달
        return redirect(url_for("main.main_func"))

    return render_template('mission.html', weeknumber=weeknumber, random_mission=random_mission)


if __name__ == '__main__':
    app.run(debug=True)
