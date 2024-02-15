def start_game():
    while True:
        print("Welcome to It All Goes Down game. \n")
        user_answer = input("Would you like to embark on this adventure? (Yes/No)\n")
        if user_answer.capitalize() == "Yes":
            print("Great, let's get started. \n")
            break
        elif user_answer.capitalize() == "No":
            print("Oh no, it's so sad to see you go. \n")
            break
        else:
            print("You've entered an invalid value, please reply with a Yes or No. \n")

start_game()