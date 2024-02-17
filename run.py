from settings import slowprint 

def intro_question():
    """
    Welcomes player to the game and asks question to begin the game
    """
    slowprint("Welcome to It All Goes Down game.\n\n")
    while True:
        slowprint("Would you like to embark on this adventure? (Yes/No)\n")
        user_answer = input("")
        if user_answer.capitalize() == "Yes":
            slowprint("\nGreat, let's get started.\n")
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
    player_name = input("\nWhat is your characters name?\n")
    while not player_name.isalpha():
        print("You have entered an invalid value!!!")
        player_name = input("What is your characters name?\n\n")
        continue
    else:
        slowprint(f"\nNice to meet you {player_name.capitalize()}. Let the adventure begin... \n")
        
        
    
    slowprint(
        "\nAfter years and years of hard work, blood, sweat and tears...\n"+ 
        "You have finally managed to save enough money to embark on\n"+
        "that journey you've been longing for since you were a child.\n\n"+
        "The destination is a magical island in the middle of the Pacific...\n"+
        "crystal clear waters and golden sands covering it's perimeter.\n\n"+
        "Your departure destination is far away from this location and\n"+
        "your budget allows you to either fly or sail there...\n\n")

def choose_transportation():
    """
    Means of transport functions, asks the user which vehicle of choice
    they prefer and unfolds storing depending on players choice.
    """
    slowprint("How would you like to travel? (Plane/Ship)\n")
    transportation_vehicle = input()
    if transportation_vehicle.capitalize() == "Plane":
        slowprint(
            "You have chosen to travel by aeroplane...\n" +
            "You arrive at the airport and check in...\n" +
            "You board the aircraft and your flight takes off...\n")
    elif transportation_vehicle.capitalize() == "Ship":
        slowprint(
            "You have chosen to travel by ship...\n" +
            "You arrive at the port, get your tickets and board the ship...\n" +
            "As soon as you locate the cabin the ship sets sale...\n" +
            "Your voyage begins...\n")
    else:
        print("You have entered an incorrect value!!!")
        print("Means of transportation needs to be either Plane or Ship")
        choose_transportation()

intro_question()
choose_transportation()