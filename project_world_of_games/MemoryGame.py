import random

result_translation = {
    False: "Lost",
    True: "Won",
    None: "Game stopped due to problem"
}

def get_difficulty_list_num(difficulty:int) -> int:
    # regturn number of elments in a lst that need to be generated based on difficulty
    return difficulty * 3

def generate_sequence(difficulty:int) -> list:
    return random.sample(range(1,101),difficulty)

def validate_user_list(listvals:list , difficalty:int)->list | None:
    if len(listvals) != difficalty:
        return None
    for value in listvals:
        if not isinstance(value, int):
            return None
        if not 1 <= value <= 101:
            return None
    return listvals.sort()

def get_list_from_user(difficulty:int) ->list | None:
    values = input(f"Enter a list of {difficulty} integer values, separated by spaces: ")
    return validate_user_list(values.split(),difficulty)

def is_list_equal(machine_list:list, user_list:list) -> bool | None:
    for position in range(len(machine_list)):
        if machine_list[position] != user_list[position]:
            return False

    return True

def play(difficulty:int) -> bool | None:
    difficulty_list_num =  get_difficulty_list_num(difficulty)
    machine_list = generate_sequence(difficulty_list_num)
    user_list =  get_list_from_user(difficulty_list_num)
    if user_list:
        is_list_equal(machine_list,user_list)
    else:
        print("User input problem")
        return None


result = result_translation[play(1)]
print(result)









