def welcome(person_name:str) -> None:
    print_str = (f"Hello {person_name} and welcome to the World of Games (WoG)."
           f"Here you can find many cool games to play.")
    return (print_str)

def load_game():

    game_selection_dict = {
        "1": "Memory Game",
        "2": "Guess Game",
        "3": "Currency Roulette"
    }

    print_str = """Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
    2. Guess Game - guess a number and see if you chose like the computer
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS"""
    print(print_str)
    selected_choice = input()

    if selected_choice not in ['1','2','3']:
        print(f"{selected_choice} is not one of the options. Please insert 1,2, or 3")
        return 0

    print_str =  "Please choose game difficulty from 1 to 5: "
    print(print_str)
    selected_difficulty =  input()
    if selected_difficulty.isnumeric() == False:
        print (f"{selected_difficulty} is not a number")
        return 0
    if int(selected_difficulty) < 1 or int(selected_difficulty) > 52:
        print(f"{selected_difficulty} is not a valid option")
        return 0

    print (f"You selected {game_selection_dict[selected_choice]} with difficulty level of {selected_difficulty}")








