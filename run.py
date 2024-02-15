def start_game():
    print("Welcome to It All Goes Down game. \n")
    user_answer = input("Would you like to embark on this adventure? (Yes/No) \n")
    if user_answer == "Yes":
        print("Great, let's get started.")
    elif user_answer == "No":
        print("Oh no, it's so sad to see you go.")
    else:
        print("You've entered an invalid value, please reply with a Yes or No.")

start_game()