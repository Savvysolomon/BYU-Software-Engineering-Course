"""
Program:            Adventure Game 
Author:             Solomon Umoh

Description:        The game compels the player to pick an option based on the question 
                    displayed on the screen. Each option picked determines the next message 
                    displayed on the screen.


"""

import sys


#Game Welcome Screen
print("=== Welcome to Desert Island Survival Adventure Game! ==== \n") 

#Game Starts Here
print("==========================================================")
print("                      START GAME                          ")
print("==========================================================")

start_keyword = str("ENTER")
abort = "Game is aborted due to wrong input. Type ENTER to proceed."

while True:
    start_game = input(f"Type '{start_keyword}' to start the game: ")

    if start_game == start_keyword:
        print("Game started! \n \n")
        break
    else:
        print(abort)
        print()
    
print("LEVEL 1 SCENARIO: THE CAVE")

print("...........................................................................")
# Level One Scenario (3 Choice Variant)
first_scene = "SCENE 1:"
second_scene = "SCENE 2:"
third_scene = "SCENE 3:"
fourth_scene = "SCENE 4:"
fifth_scene = "SCENE 5:"

print(f"You wake up on a beach. You see a dark CAVE, a thick JUNGLE, and an old BOAT.")

first_choice= input("Where do you want to go? (CAVE / JUNGLE / BOAT): ")
first_choice = first_choice.lower()

print()

#LEVEL 1 BRANCH A: CAVE
if first_choice == "cave":
    print(f"You step into the cold, damp cave. A glowing chest sits in the corner.")
    
    print("...........................................................................")
    print()

    print("LEVEL 2 SCENARIO: INSIDE THE CAVE")
    # LEVEL 2 SCENARIO (Inside Cave)
    second_choice = input(f"Do you OPEN the chest or LEAVE the cave? (OPEN / LEAVE): ")
    second_choice = second_choice.lower()
    

    # LEVEL 2 BRANCH A1: OPEN
    if second_choice == "open":
        print("The chest pops open! Inside you find a golden crown and a magical map.")

        print()
        print("...........................................................................")
        print("LEVEL 3 SCENARIO:")
        # LEVEL 3 SCENARIO (Inside Open Chest)
        third_choice = input(f"Do you WEAR the crown or follow the MAP? (WEAR / MAP): ")
        third_choice == third_choice.lower()


        if third_choice == "wear":
            print("The crown turns you into stone. Game Over!")
        elif third_choice == "map":
            print("The map guides you to a hidden rescue boat! You escape the island! You win!")
        else:
            print("Invalid choice. A snake bites you while you hesitate. Game Over!")
         
        print()
        print("...........................................................................")
    # LEVEL 2 BRANCH A2: LEAVE
    elif second_choice == "leave":
        print("You walk back outside. A massive storm starts brewing overhead.\n")


        # LEVEL 3 SCENARIO (Outside Cave Storm)
        third_choice = input("Do you HIDE under a tree or SWIM out to sea? (HIDE / SWIM): ")
        third_choice = third_choice.lower()
        
        if third_choice == "hide":
            print("Lightning strikes the tree! Game Over!\n")
        elif third_choice == "swim":
            print("A passing ship spots you swimming and rescues you! You win!\n")
        else:
            print("Invalid choice. The storm sweeps you away. Game Over!\n")
    
        
    else:
        print("Invalid choice. You slip in the darkness and fall asleep forever. Game Over!")




        print()
        print("...........................................................................")
# LEVEL 1 BRANCH B: JUNGLE
elif first_choice == "jungle":
    print("You walk into the dense jungle and discover a massive fruit tree.")
    
    # LEVEL 2 SCENARIO (Inside Jungle)
    second_choice= input("Do you EAT the fruit or CLIMB the tree to look around? (EAT / CLIMB): ")
    second_choice = second_choice.lower()
    
    # LEVEL 2 BRANCH B1: EAT
    if second_choice == "eat":
        print("The fruit tastes delicious, but it makes you incredibly sleepy.\n")
        
        # LEVEL 3 SCENARIO (Sleepy Jungle)
        third_choice= input("Do you SLEEP on the grass or RUN back to the beach? (SLEEP / RUN): ")
        third_choice = third_choice.lower()
        
        if third_choice == "sleep":
            print("A wild jaguar finds you sleeping. Game Over!\n")
        elif third_choice == "run":
            print("The adrenaline wakes you up, and you safely reach a rescue camp! You win!\n")
        else:
            print("Invalid choice. You pass out right where you stand. Game Over!")
    



    # LEVEL 2 BRANCH B2: CLIMB
    elif second_choice == "climb":
        print("From the top of the tree, you spot an active volcano starting to smoke!\n")
        
        # LEVEL 3 SCENARIO (Volcano Tree)
        third_choice = input("Do you JUMP down immediately or STAY high to watch? (JUMP / STAY): ")
        third_choice = third_choice.lower()
        
        if third_choice == "jump":
            print("You land safely and escape the lava flow just in time! You win!\n")
        elif third_choice == "stay":
            print("The toxic smoke overwhelms you. Game Over!\n")
        else:
            print("Invalid choice. The tree shakes and you fall. Game Over!\n")
        
    else:
        print("Invalid choice. Monkeys throw rocks and chase you away. Game Over!")
    

    print()
    print("...........................................................................")
# LEVEL 1 BRANCH C: BOAT
elif first_choice == "boat":
    print("You inspect the rotten boat. There is a hole in the bottom, but a radio is inside.")
    
    # LEVEL 2 SCENARIO (At the Boat)
    second_choice = input("Do you FIX the hole or try to use the RADIO? (FIX / RADIO): ")
    second_choice = second_choice.lower()

    
    # LEVEL 2 BRANCH C1: FIX
    if second_choice == "fix":
        print("You patch the hole with leaves and mud, then push out into the water.\n")
        
        # LEVEL 3 SCENARIO (Fixed Boat)
        third_choice = input("Do you ROW toward the horizon or FISH for food? (ROW / FISH): ")
        third_choice == third_choice.lower()
        
        if third_choice == "row":
            print("You reach a shipping lane and get picked up by a cruise ship! You win!\n")
        elif third_choice == "fish":
            print("A giant shark capsizes your weak patch job. Game Over!\n")
        else:
            print("Invalid choice. The boat drifts out into a whirlpool. Game Over!")
        

        print()
        print("...........................................................................")    
    # LEVEL 2 BRANCH C2: RADIO
    elif second_choice == "radio":
        print("The radio crackles to life! You hear a faint rescue signal.\n")
        
        # LEVEL 3 SCENARIO (Radio Signal)
        third_choice= input("Do you SHOUT into the mic or WAIT for them to talk? (SHOUT / WAIT): ")
        third_choice = third_choice.lower()
        
        if third_choice == "shout":
            print("The coast guard hears your shouting and locks onto your position! You win!\n")
        elif third_choice == "wait":
            print("The radio battery dies completely before you say anything. Game Over!\n")
        else:
            print("Invalid choice. You drop the radio in the water. Game Over!\n")
    
        
    else:
        print("Invalid choice. The boat collapses on top of you. Game Over!")
    

# LEVEL 1 GLOBAL ELSE
else:
    print("Invalid choice. You sat on the beach too long and got severe sunburn. Game Over!\n")


sys.exit()


