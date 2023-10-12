from flask import Flask, request, render_template, Blueprint, redirect
from pymongo import MongoClient
from modules.userdatas import krafton_paticipants
import random
from bson import ObjectId

client = MongoClient('localhost', 27017)
db = client.kraftto
admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/admin', methods=['GET', 'POST'])
def admin_func():
    not_approved_message = list(db.message.find({'is_approved': False}))
    # print(not_approved_message)

    return render_template('admin.html', messages=not_approved_message)


@admin_bp.route('/admin/update', methods=['GET', 'POST'])
def admin_approve():
    _id = request.args.get('_id')
    obj_id = ObjectId(_id)

    # Use the correct query condition to find the document by its ObjectId
    db.message.update_one({"_id": obj_id}, {'$set': {'is_approved': True}})

    not_approved_message = list(db.message.find({'is_approved': False}))
    print(not_approved_message)
    return render_template('admin.html', messages=not_approved_message)
