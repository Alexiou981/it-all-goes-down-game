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
            "that one of the engine turbines is on fire...\n"+
            "Only now you realise that theres something terrible going on...\n"+
            "You hear a loud noise, the lights go off and the oxygen masks drop...\n")
        slowprint_ascii(bang)
        slowprint(
            "\nA loud noise sounds as if something exploded...\n"
            "You can feel that the airplane is descending and\n"+ 
            "accelerating at the same time...\n"+
            "The captain announces that his lost full control of the aircraft...\n"+
            "People are losing control and all you can hear is screaming and crying...\n\n"+
            "The crew is shouting... BRACE BRACE BRACE!\n"+
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
            "Stay at the beach, try to find food and water and rest a bit more?\n"+
            "(Beach/Explore)?"
            )
        beach_or_explore()
        
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
        slowprint(
            "You jumped in the water...\n"+
            "It's colder than you expected it to be...\n"+
            "The waves are massive and you are struggling to surface...\n\n"+
            "You did not get a life jacket before you jump...\n"+
            "Your clothes are soaked and they're getting heavier...\n"+
            "Regardless the efforts and due to the high waves...\n\n"+
            "You couldn't survive and you drown... :(\n"+
            "GAME OVER!!!\n\n"+
            "WOULD YOU LIKE TO TRY AGAIN ??? (Yes/No)\n")
        try_again()
    elif jump_stay.capitalize() == "Stay":
        slowprint(
            "You decide to stay...\n"+
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
            "Stay at the beach, try to find food and water and rest a bit more?\n"+
            "(Beach/Explore)?\n"
            )
        beach_or_explore()
    else:
        print("You've entered an invalid value, please reply with Jump or Stay")
        jump_or_stay()


def try_again():
    """
    This function takes the user answer Yes or No and acts accordingly.
    If no value is added then it prints and error message explaining,
    which values are valid.
    """
    while True:
        try_again_answer = input()
        if try_again_answer.capitalize() == "Yes":
            os.system("clear")
            main()
            break
        elif try_again_answer.capitalize() == "No":
            slowprint("It's so sad to see you go... Thanks for playing the game :D\n")
            slowprint("\nGoodbye for now!!!\n\n")
            slowprint("This game was created for educational purposes by Evangelos Alexiou\n")
            break
        else:
            print("You have entered an invalid value, please reply with Yes or No")


def drink_from_lake():
    while True:
        drink_answer = input()
        if drink_answer.capitalize() == "Yes":
            slowprint("You drink plenty of water rehydrate yourself...\n"+
                  "And continue to your adventure...\n"+
                  "In the search of food, shelter and more water...\n\n"+
                  "You move a little bit further inside the forrest...\n"+ 
                  "You come accross some fruit trees. As you get closer realise...\n" +
                  "Those trees are banana trees and have plenty of fruits on them...\n\n"+ 
                  "You climb one of them and gather a bunch,\n"+ 
                  "You eat and regain back all the energy that you lost during the crash...\n"+ 
                  "You start to feel normal again and start walking accross the forest...\n"+
                  "Ready to face any challenge...\n\n"+
                  "After a while...\n"+
                  "Having walked for several hours you path diverges in two...\n"+
                  "On your left hand side, the path goes uphill...\n"+
                  "On your right hand side, the path goes downhill but\n"+
                  "seems to be steeper...\n\n"+
                  "This is your time to take an important decision for your survival...\n"+
                  "Would you like to go Uphill or Downlhill? (Uphill/Downhill)\n")
            uphill_downlhill()
            break
        elif drink_answer.capitalize() == "No":
            slowprint("You decide not to drink...\n"+
                  "Having walked for hours and hours,\n"+
                  "Unable to find any other source of water...\n\n"+
                  "You die from dehydtration...\n"+
                  "GAME OVER :(\n\n"+
                  "WOULD YOU LIKE TO TRY AGAIN ??? (Yes/No)\n")
            try_again()
            break
        else:
            print("You've entered an invalid value. Please reply Yes or No ")


def beach_or_explore():
    """
    This function takes the user decision Beach or Explore and executes code,
    depending on users decision. It also ensure that no invalid values are being
    input and explains to the user which values are valid.
    """
    while True:
        beach_or_explore = input()
        if beach_or_explore.capitalize() == "Beach":
            slowprint("You stayed at the beach...\n"+
                  "You didn't find anything around, the night came in...\n"+  
                  "It's too late now to visit the forest without any light or fire.\n\n"+
                  "Since you haven't eaten or drunk for a long time,\n" 
                  "dehydtation kicks in and you end up dying on the beach...\n"
                  "GAME OVER :(\n" 
                  "WOULD YOU LIKE TO TRY AGAIN ??? (Yes/No)")
            try_again()
            break
        elif beach_or_explore.capitalize() == "Explore":
            slowprint("You decice to explore the forest...\n"+
                  "You head towards it...\n"+
                  "After having entered the tropical forest and walked for several hours...\n"+
                  "you came across a lake with fresh water, with many fish swimming in it\n"+ 
                  "and animals drinking water from it...\n\n"+ 
                  "After so many hours of being unconsious you feel extremely dehydrated...\n"+ 
                  "Would you like to drink from the lake? (Yes/No)\n")
            drink_from_lake()
            break
        else:
            print("You've entered an invalid value. Please reply Beach or Explore")
    
def uphill_downlhill():
    """
    This function unveals the story depending on which path the player has decided 
    to take. It also prints an error message if an empty or invalid answer has been 
    typed in.
    """
    while True:
        uphill_downhill_answer = input()
        if uphill_downhill_answer.capitalize() == "Uphill":
            slowprint("You've decided to go uphill...\n"+
                  "You choose to start walking up the little mountain...\n\n"+ 
                  "After a few minutes of climbing you find a what appears to be like a trail,\n"+ 
                  "this is a good sign that other people have definitely been here before...\n"+ 
                  "Your hopes for survival raise significantly...\n\n"+
                  "You continue walking uphill and after a while of more walking...\n"+
                  "The ground seems to start leveling and the top is closer than ever...\n\n"+
                  "As you reach the top of the hill, and to your surprise...\n"+
                  "You can see what appears to be a shelter...\n"+
                  "Possibly build for those who go trailing there...\n\n"+
                  "You run inside the shelter hoping to come accross another human being...\n"+
                  "Desperate for help, food and medical care...\n"+
                  "You're dissappointed to find that nobody is in...\n\n"+
                  "To your own luck however, you find working facilities and beds...\n"+
                  "This means that you can survive the night inside the shelter...\n"+
                  "You have a look around the shelter...\n\n"+
                  "You couldn't find any food anywhere...\n"+
                  "However, you managed to spot some items that might appear useful later on...\n"+
                  "Inside a small box you find...\n"+ 
                  "a sack, clothing, matches, a knife, bottled water,\n"+ 
                  "rope and a pair of binoculars...\n\n"+
                  "You start to feel tired and decide to get some rest...\n\n"+
                  "The next day as soon as the sun rises...\n"+
                  "You get ready to continue your search for food and medical care...\n"+
                  "The sack and items you found yesterday might appear to be useful...\n"+
                  "You decide to take it and include inside the items you found...\n\n"+
                  "It is a sunny day and the atmosphere clear of fog...\n"+
                  "The shelter being located at the top of a hill,\n"+
                  "gives you great visibility of the surrounding landscape...\n\n"+
                  "You have a look around and try to decide which way to go...\n"+
                  "On the West side of the shelter and far into the horizon...\n"+
                  "Appear to be a few buildings or warehouses...\n\n"+
                  "On the East side of the shelter, behind some trees...\n"+
                  "You can spot some smoke coming up...\n" 
                  "Coult it be humans???\n\n"+
                  "Now it's the time for a decision to be made...\n"+
                  "Your life depends on it...\n"+
                  "Would you like to go West or East? (West/East)\n")
            west_or_east()
            break
        elif uphill_downhill_answer.capitalize() == "Downhill":
            slowprint("You've decided to go downhill...\n"+
                  "You start to make your way downhill carefully...\n"+
                  "Despite the slippery ground you managed to get down,\n"+ 
                  "where the ground was flat again...\n"+ 
                  "This part of the island seems to be more rocky and desserted...\n\n"+
                  "You walk for many miles and come accross what seems to be a cave...\n"+
                  "That could possibly be your shelter for the night...\n"+
                  "As you get closer you spot a backpack by the entrance of the cave...\n"+
                  "Your hopes that there's other people on the island get up...\n\n"+
                  "You decide to enter the cave and shout to see if anyone is inside...\n"+
                  "You don't hear anything back and assume you're alone...\n"+
                  "If there's nobody inside then whose is that backpack?\n\n"+
                  "The night has fallen and you are tired...\n"+
                  "Inside the cave it's pitch black and silent...\n"+
                  "The silence and darkness nearly drive you mad...\n"+
                  "Different scenarios of what could go wrong go through your mind...\n\n"+
                  "Eventually you manage to fall asleep and rest until the morning...\n"+
                  "During the night things get an unexpected turn...\n"+
                  "A poisonus snake bites you and you end up dying inside the cave...\n\n"
                  "GAME OVER :(\n"
                  "WOULD YOU LIKE TO TRY AGAIN ??? (Yes/No)\n")
            try_again()
            break
        else:
            print("You've entered an invalid value. Please reply with Uphill or Downhill.")


def west_or_east():
    """
    This function gets the users decision to head West or East and unfolds the story
    depending on the choice. It also prints an error if an empty or invalid values
    has been typed in.
    """
    while True:
        west_east_answer = input()
        if west_east_answer.capitalize() == "West":
            slowprint("You decide to go West...\n"+
                  "You make your way toward what appeared to be buildings...\n\n"+
                  "Suddenly, you hear a ruslting noise from inside the woods...\n"+
                  "You turn around and realise that there is a Wild Boar\n"+
                  "Looking towards you, preparing to attack...\n\n"+
                  "You time is limited and your decision is necessary...\n"+
                  "Do you try to defend yourself using the knive?\n"+
                  "OR\n"+
                  "You start running trying to protect yourself from danger?\n"+
                  "(Fight/Flight)?"
                  )
            fight_flight_wboar()
            break
        elif west_east_answer.capitalize() == "East":
            slowprint("You decide to go East...\n"+
                  "You start walking towards the direction that smoke was coming from...\n"+
                  "Luckily, the destination is not very far and within hours...\n"+
                  "You walk your way there and you finally arrive...\n\n"+
                  "The closer you get the darker and thicker the smoke gets...\n"+
                  "Soon you realise that this fire was not intentional...\n"+
                  "The fire is spreading at a fast pace and the wind makes it worse...\n\n"+
                  "The time is limited and a decision needs to be made...\n"+
                  "Would you try to Stop the fire or Seek Out for help?\n"+
                  "(Stop/Help)\n")
            stop_fire_seek_help()
            break
        else:
            print("You've entered an invalid value. Please reply West or East")


def fight_flight_wboar():
    while True:
        fight_flight_answer = input()
        if fight_flight_answer.capitalize() == "Fight":
            slowprint("You fight as hard as you can for your life...\n"+
                  "You managed to stab it with the knife but it didn't seem to work...\n"+
                  "You're knife is stuck where you've previously stabbed it...\n"+
                  "Your only weapon now are your bear hands...\n\n"+
                  "After several minutes of fighting and struggling...\n"+
                  "One of it's horns pierces right through your belly...\n"+
                  "You bleed to death...\n\n"+
                  "GAME OVER :(\n"
                  "WOULD YOU LIKE TO TRY AGAIN? (Yes/No)")
            try_again()
            break
        elif fight_flight_answer.capitalize() == "Flight":
            slowprint("You run away as fast as you can gor you life...\n"+
                  "You're looking for a shelter to protect you from the threat..\n"+
                  "As you continue running you come across a tall tree...\n\n"+
                  "You manage to climb on it fast enough to avoid the boar...\n"+
                  "You wait on top of the tree patiently...\n"+
                  "Almost one hour has passed by and you are looking around\n"+
                  "to ensure that the danger is now gone and the ground is safe...\n\n"+
                  "You start making your way down and heading West...\n"+
                  "You've used up so much energy during the chase and you feel\n"+
                  "exhausted and extremely hungry...\n\n"+
                  "Regardless the fatigue, the hunger and the pain you continue walking...\n"+
                  "The more you walk you start to realise that the trees are getting\n"+
                  "less and less, and those buildings seem to be closer than ever now...\n\n"+
                  "As you're getting closer you're being approached by two uniformed men...\n"+
                  "They see the condition you are in...\n"+
                  "And they offer to help you immediately...\n\n"+
                  "They take you to the nearest hospital and take you to the emergencies...\n"+
                  "The doctors and nurser take great care of you...\n"+
                  "A few moments later and having regained your strength...\n\n"+
                  "You get in touch with your embassy and report as a survivor\n"+
                  "of this tragedy...\n"+
                  "To your surprise they inform you that you're the only survivor so far...\n"+
                  "They also inform you that no ruins have been found yet...\n\n"+
                  "Finally, you manage to get in touch with your family\n"+
                  "and inform them that you are safe and sound...\n\n"+
                  "Well done for surviving this adventure!!!\n"+
                  "You might have lost the vacation of your dreams...\n"+
                  "But you have certainly Won in Life!\n\n"+
                  "Thanks for playing It All Goes Down!\n"+
                  "Would you like to play again? (Yes/No)")
            try_again()
            break
        else:
            print("You've entered an invalid value. Please reply Fight or Flight.")


def stop_fire_seek_help():
    """
    This function gets the users decision to try to Stop the fire or Seek out for help,
    depending on the choice the story takes a different turn. It also prints an error
    if invalid or empty value has been input.
    """
    while True:
        stop_help_answer = input()
        if stop_help_answer.capitalize() == "Stop":
            slowprint("You've chosen to try and put out the fire...\n"+
                  "Having panicked as you came across it...\n"+
                  "You use the bottled water from inside your sack...\n\n"+
                  "This was not effective at all...\n"+
                  "The flames have gotten bigger and bigger...\n"+
                  "The smokes is so thick and by inhaling it you pass out...\n\n"+
                  "The flames cover your body and you get roasted.\n"
                  "GAME OVER :(\n"
                  "WOULD YOU LIKE TO TRY AGAIN ??? (Yes/No)")
            try_again()
            break
        elif stop_help_answer.capitalize() == "Help":
            slowprint("You've decided to seek out for help...\n"+
                  "You run as fast as you can giving everything you've got...\n"+
                  "Luckily, you soon come accross a small vilage...\n\n"+
                  "There are a few people out on the streets...\n"+
                  "You find the first person you see in front of you,\n"+
                  "and after managing to catch your breath you start explaining...\n\n"+
                  "You prioritise mentioning about the fire and firefighters\n"+
                  "are on the way to put out the fire...\n\n"+
                  "You then explain to them about the tragedy you were in...\n"+
                  "One of the villagers offers to give you a lift to the hospital...\n"+
                  "There's no immediate access to an ambulance in that area...\n"+
                  "And so he gives you a lift on a motorbike...\n\n"+
                  "As you arrive at the hospital, doctors and nurses\n"+
                  "take great care of you...\n"+
                  "Once you starting to feel better...\n\n"+
                  "You get in touch with your embassy and inform them you're a survivor...\n"+
                  "They are surprised to hear that and reassure you a safe return at home...\n"+
                  "To your surprise they inform you that so far you're the only survivor\n"+
                  "of the crash...\n\n"+
                  "The embassy manages to get you in touch with your family...\n"+
                  "You inform them that you're safe and sound...\n"+
                  "They sound delighted and extremely relieved...\n\n"+
                  "In the meantime, the firefighters have managed to put it out...\n"+
                  "They return to the hospital to thank you for informing them...\n"+
                  "They're calling you a true hero...\n\n"+
                  "Well Done for making out alive...\n"+
                  "You might have lost the chance to visit your dream destination\n"+
                  "but you did manage to Win Life!!!\n\n"+
                  "Thanks for playing It All Goes Down :D\n"+
                  "Would you like to play again? (Yes/No)\n\n")
            try_again()
            break
        else:
            print("You've entered an invalid value. Please reply Stop or Help.\n")




def main():
    """
    This function includes the two basic functions that start the game,
    use this and call the main function which will run any functions called in it,
    instead of having to call each function individually.
    """
    intro_question()
    choose_transportation()

main()