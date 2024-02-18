import os

from settings import (
                    slowprint,
                    slowprint_ascii
)
from ascii import (
                    airplane_or_ship,
                    ship,
                    airplane,
                    bang
    )

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
        slowprint_ascii(airplane)
        slowprint(
            "\nEverything is running smoothly and the aircraft has now leveled...\n"+
            "The fasten your seatbelts sign swithes off...\n"+
            "Soon the mini bar service will be available...\n"+
            "While you're waiting your browsing through the movies availabel to you...\n\n"+
            "The cabin crew arrives with the food and drinks trolley...\n"+
            "You choose to get a drink, since you're tired and want to get some sleep...\n\n"+
            "A few moments later and whilst you're half asleep...\n"+
            "You hear the captain announcing that we're expecting some sort of turbulence...\n"+
            "The fasten your setbelt sign turns on and everyone is asked\n"+
            "to return to their seats...\n\n"+
            "As you look out of the window you realise,\n"+ 
            "that one of the wind turbines is on fire...\n"+
            "Only now you realise that theres something terrible going on...\n"+
            "You hear a loud noise, the lights go off and the oxygen masks drop...\n")
        slowprint_ascii(bang)
        slowprint(
            "\nA loud noise sound as if something exploded...\n"
            "You can feel that the airplane is descending and\n"+ 
            "accelerating at the same time...\n"+
            "The captain announces that his lost full control of the aircraft...\n"+
            "People are losing control and all you can hear is screaming and crying...\n\n"+
            "The crew shouting... BRACE BRACE BRACE!\n"+
            "You brace for impact, everything happens so fast and you try to remain calm...\n"+
            "Everything goes dark, the plane crashes and you are unconsious...\n\n"+
            "DARKNESS EVERYWHERE...\n\n"
            "A few hours later...\n\n"+
            "You wake up on a beach with barely any clothes on left from the tragedy...\n"+
            "You feel your whole body aching and extremely dehydrated...\n"+
            "The sun is getting hotter and hotter...\n\n"+
            "You need to find yourself shelter, clothing, water and food...\n"+
            "You look left and right...\n"+
            "And realise that there is some sort of a forest at the end of the beach...\n\n"+
            "Would you like to explore the forrest for any useful objects for survival?\n"+
            "OR\n"+
            "Stay at the beach, try to find food and water and rest a bit more?\n"
            )
        
    elif transportation_vehicle.capitalize() == "Ship":
        slowprint(
            "You have chosen to travel by ship...\n"+
            "You arrive at the port, get your tickets and board the ship...\n"+
            "As soon as you locate the cabin the ship sets sale...\n\n")
        slowprint_ascii(ship)
        slowprint(    
            "\nYour voyage begins and everything seems to be running smooth...\n"+
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
    """
    This function checks what has the user decided whether to 
    Jump or Stay and prints output depending on decision.
    """
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
        jump_game_over()
    elif jump_stay.capitalize() == "Stay":
        slowprint("You decide to stay...\n"+
                  "Even though at first it seemed like an unwise choice...\n"+
                  "The crew has managed to distribute lifejackets to everyone...\n"+
                  "After having been fully equipped, you're being instructed\n"+
                  "to evacuate the ship safely...\n\n"+
                  "You're now inside the water and you can barely see the ship,\n"+
                  "as most of it is sunk already...\n"+
                  "The temperature of the water is really low and the waves are massive...\n\n"+
                  "Despite your efforts to stand still and remain in groups,\n"+
                  "strong currents take you away and whilst trying to go against them...\n"+
                  "You exhaust yourself and fall unconsioucs, a big wave hits you...\n\n"+
                  "Everything goes dark...\n\n"+
                  "A few hours later...\n\n"+
                  "You wake up on a beach with barely any clothes on left from the tragedy...\n"+
                  "You feel your whole body aching and extremely dehydrated...\n"+
                  "The sun is getting hotter and hotter...\n\n"+
                  "You need to find yourself shelter, clothing, water and food...\n"+
                  "You look left and right...\n"+
                  "And realise that there is some sort of a forest at the end of the beach...\n\n"+
                  "Would you like to explore the forrest for any useful objects for survival?\n"+
                  "OR\n"+
                  "Stay at the beach, try to find food and water and rest a bit more?\n"
                  )
    else:
        print("You've entered an invalid value, please reply with Jump or Stay")
        jump_or_stay()


def jump_game_over():
    """
    Jump decision leads to game over, this function asks user if they want to play again,
    depending on the inpup the game either restarts, print goodbye message to user or 
    outputs error message when an empty value was input or anything else but Yes or No.
    """
    while True:
        game_over_jump = input()
        if game_over_jump.capitalize() == "Yes":
            os.system("clear")
            main()
            break
        elif game_over_jump. capitalize() == "No":
            slowprint("It's so sad to see you go... Thanks for playing the game :D\n")
            slowprint("\nGoodbye for now!!!\n\n")
            break
        else:
            print("You have entered an invalid value, please reply with Yes or No")
            

def main():
    intro_question()
    choose_transportation()

main()