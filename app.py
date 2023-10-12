from flask import Flask, render_template, request, session, redirect, url_for, flash, jsonify
from pymongo import MongoClient
from modules.login import login_bp
from modules.signup import signup_bp
from modules.main import main_bp
from modules.mission_complete import mission_complete_bp
from modules.mission import mission_bp

from modules.ramdom_manito import krafton_paticipants, user_datas


app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.kraftto


@app.route('/')
def main():
    return render_template('index.html')


# login
app.register_blueprint(login_bp)

# signup
app.register_blueprint(signup_bp)

# main
app.register_blueprint(main_bp)

# mission
app.register_blueprint(mission_bp)

# mission Complete
app.register_blueprint(mission_complete_bp)


if __name__ == '__main__':
    app.run(debug=True)
