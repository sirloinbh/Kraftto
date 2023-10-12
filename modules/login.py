import hashlib
import datetime

import jwt
from flask import Flask, request, render_template, Blueprint, redirect, url_for, jsonify
from pymongo import MongoClient

SECRET_KEY = 'secrete key'

client = MongoClient('localhost', 27017)
db = client.kraftto

login_bp = Blueprint('login', __name__)


@login_bp.route('/login', methods=['GET'])
def login_func():
    return render_template('login.html')
