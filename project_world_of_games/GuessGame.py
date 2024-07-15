import random

def get_difficulty_range(difficulty:int)->int:
    return difficulty * 10

def generate_number(difficulty:int)-> str:
    return random.randint(1,difficulty+1)


def get_guess_from_user(difficulty:int) -> int:
    input_data = input (f"Insert number between 1 and {difficulty}: ")
    if input_data.isnumeric() and 1 <= int(input_data) <= difficulty:
        return int(input_data)
    else:
        print(f"Invalid input. Please enter a valid integer between 1 and {difficulty}")
        return -1


def compare_results(secret_number:int , guess_number:int)-> bool:
    return secret_number == guess_number


def play(difficulty) -> bool | None:
    difficulty_range = get_difficulty_range(difficulty)
    secret_number = generate_number(difficulty_range)
    guess_number =  get_guess_from_user(difficulty_range)
    if guess_number == -1:
        print ("Game stopped")
        return None

    return compare_results(secret_number,guess_number)


ret_value =  play(1)
if ret_value == True:
    print("You won")
elif ret_value == False:
    print("you lost")
else:
    print("game stopped")




        