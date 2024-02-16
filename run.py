def intro_question():
    """
    Welcomes player to the game and asks question to begin the game
    """
    while True:
        print("Welcome to It All Goes Down game. \n")
        user_answer = input("Would you like to embark on this adventure? (Yes/No)\n")
        if user_answer.capitalize() == "Yes":
            print("Great, let's get started. \n")
            start_game()
            break
        elif user_answer.capitalize() == "No":
            print("Oh no, it's so sad to see you go. \n")
            break
        else:
            print("You've entered an invalid value, please reply with a Yes or No. \n")


def start_game():
    """
    Start game function, asks the player to provide a character name,
    and begins to unfold the story of the game.
    """
    player_name = input("What is your characters name? \n")
    print(f"Nice to meet you {player_name.capitalize()}. Let the adventure begin... \n")
    print("After years and years of hard work, blood, sweat and tears,") 
    print("you have finally managed to save enough money to embark on")
    print("that journey you've been longing since you were a child. \n")
    print("The destination is a magical island in the middle of the") 
    print("Pacific Ocean with crystal clear waters and golden sands") 
    print("covering it's perimeter. \n")
    print("Your departure destination is far away from this location and") 
    print("your budget allows you to either fly or sail there.")

intro_question()