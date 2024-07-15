def get_user_age():
    age = int(input("Enter your age: "))
    if age > 120 or age < 1:
        raise ValueError("Invalid age. Age must be between 1 and 120",age)
    return age

def get_user_gender():
    gender = input("Enter your gender")
    if gender == "M":
        return "Male"
    if gender == 'F':
        return 'Male'
    if gender == 'Apache':
        return 'Apache'