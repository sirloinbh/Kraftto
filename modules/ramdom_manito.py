import random

krafton_paticipants = {
    0: "마찬옥",
    1: "김진규",
    2: "김병현",
}

user_data = []


def create_user_data():
    random_recipient_num = random.choice(range(3))
    new_user_data = {
        "name":  "마찬옥",
        "email": "a01049149446@gmail.com",
        "passwrod": "1234",
        "hint":  {
            "which_os": "mac",
            "sex": "man",
        },
        "recipient": krafton_paticipants[random_recipient_num]
    }

    del krafton_paticipants[random_recipient_num]
    user_data.append(new_user_data)
    return user_data


create_user_data()
print(user_data)
print(krafton_paticipants)