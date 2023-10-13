from pymongo import MongoClient
client = MongoClient('mongodb://sun:shine@13.209.47.134', 27017)
db = client.kraftto

weekly_missions = {
    "mission1": "손인사하기",
    "mission2": "How's your jungle life? 물어보기",
    "mission3": "커피 자리에 몰래 놔두기",
    "mission4": "조그만한 간식 건내주기",
    "mission5": "함께 화이팅 외쳐주기",
    "mission6": "어느 지역에서 왔는지 물어보기",
    "mission7": "SNS 물어보기",
    "mission8": "함께 학식 먹자고 물어보기",
    "mission9": "함께 5분간 산책하자고 물어보기",
    "mission10": "모르는 문제 알려주기",
    "mission11": "함께 운동하기",
    "mission12": "'힘내세요' 쪽지 전달하기",
    "mission13": "함께 오르막길 오르기",
    "mission14": "무거운 짐 들어주기",
    "mission15": "고민 들어주기",
    "mission16": "따뜻한 아침인사 건내기",
}


def insert_mission_db():
    for mission in weekly_missions.items():
        db.mission.insert_one(
            {'mission': mission[0], "description": mission[1]})
