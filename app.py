from flask import Flask, render_template, request, session, redirect, url_for, flash, jsonify
from pymongo import MongoClient
from modules.login import login_bp, SECRET_KEY
from modules.signup import signup_bp
from modules.main import main_bp
from modules.mission_complete import mission_complete_bp
from modules.mission import mission_bp
from modules.admin import admin_bp


app = Flask(__name__)
client = MongoClient('mongodb://sun:shine@13.209.47.134', 27017)
db = client.kraftto

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

# admin
app.register_blueprint(admin_bp)


@app.route('/')
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
