from settings import slowprint 

def intro_question():
    """
    Welcomes player to the game and asks question to begin the game
    """
    slowprint("Welcome to It All Goes Down game. \n")
    while True:
        slowprint("Would you like to embark on this adventure? (Yes/No)")
        user_answer = input()
        if user_answer.capitalize() == "Yes":
            slowprint("Great, let's get started. \n")
            start_game()
            break
        elif user_answer.capitalize() == "No":
            slowprint("Oh no, it's so sad to see you go. \n")
            break
        else:
           print("You've entered an invalid value, please reply with a Yes or No. \n")


def start_game():
    """
    Start game function, asks the player to provide a character name,
    and begins to unfold the story of the game.
    """
    player_name = input("What is your characters name? \n")
    while player_name.isnumeric():
        print("You have entered an invalid value!!!")
        player_name = input("What is your characters name? \n")
    else:
        slowprint(f"Nice to meet you {player_name.capitalize()}. Let the adventure begin... \n")
    
    slowprint("After years and years of hard work, blood, sweat and tears...") 
    slowprint("You have finally managed to save enough money to embark on")
    slowprint("that journey you've been longing for since you were a child. \n")
    slowprint("The destination is a magical island in the middle of the Pacific...") 
    slowprint("Crystal clear waters and golden sands covering it's perimeter. \n") 
    slowprint("Your departure destination is far away from this location and") 
    slowprint("your budget allows you to either fly or sail there... \n")

intro_question()