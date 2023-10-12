from flask import Flask, request, render_template, Blueprint
from pymongo import MongoClient
from modules.userdatas import krafton_paticipants
import random


client = MongoClient('localhost', 27017)
db = client.kraftto
admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin', methods=['GET', 'POST'])
def admin_func():
    return render_template('admin.html')

