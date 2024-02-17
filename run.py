from settings import (
                    slowprint,
                    slowprint_ascii
)
from ascii import airplane_or_ship

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
        "Crystal clear waters and golden sands covering it's perimeter.\n\n"+
        "Your departure destination is far away from this location and\n"+
        "your budget allows you to either fly or sail there...\n\n")

def choose_transportation():
    """
    Means of transport functions, asks the user which vehicle of choice
    they prefer and unfolds storing depending on players choice.
    """
    slowprint_ascii(airplane_or_ship)
    slowprint("\nHow would you like to travel? (Plane/Ship)\n")
    transportation_vehicle = input()
    if transportation_vehicle.capitalize() == "Plane":
        slowprint(
            "You have chosen to travel by aeroplane...\n" +
            "You arrive at the airport and check in...\n" +
            "You board the aircraft and your flight takes off...\n")
    elif transportation_vehicle.capitalize() == "Ship":
        slowprint(
            "You have chosen to travel by ship...\n"+
            "You arrive at the port, get your tickets and board the ship...\n"+
            "As soon as you locate the cabin the ship sets sale...\n\n"+
            "Your voyage begins and everything seems to be running smooth...\n"+
            "You get yourself comfortable in your luxurious cabin,\n"+
            "and decide to head to the bar...\n\n"+
            "After having tried a few of their finest drinks you start to feel tired...\n"+
            "You return to your cabin and decide to get some sleep...\n\n"+
            "Several hours later...\n\n"+
            "A loud noise and an impact that felt like the ship crashed onto something...\n"+
            "You get outside and realise that there is an emergency evacuation\n" 
            "procedure happening...\n"+
            "\nEveryone is at a state of panic trying to make their way\n"+
            "to the nearest emergency boat...\n"+
            "People start to lose control and push each other in order to\n"+
            "get through to one of those boats...\n\n"+
            "As the time goes by things start to get even worse\n"+
            "and you realise that the ship is starting to flip over...\n"
            "All of the emergency boats are fully occupied by now...\n"+
            "The time is limited and there's a decision to be made...\n\n"+
            "Jump in the water and try to survive swimming?\n"+
            "OR\n"+
            "Try to remain calm and wait for instructions from the crew?\n\n"+
            "What do you do? (Jump/Stay)\n")
        jump_or_stay()
    else:
        print("You have entered an incorrect value!!!")
        print("Means of transportation needs to be either Plane or Ship")
        choose_transportation()

def jump_or_stay():
    jump_stay = input()
    if jump_stay.capitalize() == "Jump":
        slowprint("You jumped in the water...\n"+
                  "It's colder than you expected it to be...\n"+
                  "The waves are massive and you are struggling to surface...\n\n"+
                  "You did not get a life jacket before you jump...\n"+
                  "Your clothes are soaked and they're getting heavier...\n"+
                  "Regardless the efforts and due to the high waves...\n\n"+
                  "You couldn't survive and you drown... :(\n"+
                  "GAME OVER!!!\n\n"+
                  "WOULD YOU LIKE TO TRY AGAIN ??? (Yes/No)\n")
        game_over_jump = input()
        slowprint(game_over_jump)
    elif jump_stay.capitalize() == "Stay":
        print("You decide to stay...")
    else:
        print("You've entered an invalid value, please reply with Jump or Stay")
        jump_or_stay()


def main():
    intro_question()
    choose_transportation()

main()