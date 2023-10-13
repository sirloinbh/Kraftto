import hashlib

from pymongo import MongoClient

client = MongoClient('mongodb://sun:shine@13.209.47.134', 27017)
db = client.kraftto

db.user.insert_one({'username': 'admin', 'email': 'admin', 'password': hashlib.sha256('a'.encode('utf-8')).hexdigest(),
                    'OS': 'windows', 'gender': '남자', 'junglenumber': '홀수', 'is_manitto': False, 'person_i_help': '',
                    'person_i_got_help': '', 'current_mission': ''})
