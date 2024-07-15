def get_user_age():
    age = int(input("Enter your age: "))
    if age > 120 or age < 1:
        raise ValueError("Invalid age. Age must be between 1 and 120",age)
    return age

try:
    age = get_user_age()
    print(age)
except BaseException as e:
    print(e)
