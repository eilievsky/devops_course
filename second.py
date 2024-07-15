from first import get_user_gender, get_user_age

def get_user_data():
    user = {}
    user['age'] =  get_user_age()
    user['gender'] =  get_user_gender()
    return user

