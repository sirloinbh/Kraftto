from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)


@app.route('/mission', methods=['GET', 'POST'])
def get_user_data():
    # 랜덤으로 지정된 자신의 마니또 데이터를 불러오기.
    return render_template(f'mission.html')


@app.route('/mission/<id>', methods=['GET', 'POST'])
def weekly_mission():
    if request.method == "POST":
        message = request.form.get(message)
        # POST = Message -> DB 전달
        return redirect(url_for("get_user_data"))

    # 주차별로 html 렌더링함.
    return render_template(f'mission.html', id=id )


@app.route('/mission/<id>/complete', methods=['GET', 'POST'])
def weekly_mission_complete():
    # 미션 완료 페이지 렌더링
    # DB에서 자신의 마니또의 힌트를 가지고와서 보여줌

    # if id == 4 일 경우, Final mission Page를 가지고온다.
    # 1~4주차 메세지 모두를 불러온다.
    return render_template(f'mission/{id}/complete.html')


if __name__ == '__main__':
    app.run(debug=True)
