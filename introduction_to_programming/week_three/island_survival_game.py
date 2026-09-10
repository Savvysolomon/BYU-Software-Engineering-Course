"""

Program:            Adventure Game (Desert Island Survival)

Author:             Solomon Umoh

Description:        This game is a choice-driven text adventure set on a desert island.
                    Player explore locations like the beach, cave, jungle, and boat; 
                    and make decisions that results in either win or game over. 


                    
Addition:           Player cannot proceed into the game without typing the correct word "ENTER".
                    Game aborts and returns player to the entry point if the wrong word is typed.
                    .strip().upper() is used to ensure that the game proceeds however the player 
                    typed the "enter", "Enter", or "ENTER" keyword.             


"""   




# Game Welcome Screen
print("=== Welcome to Desert Island Survival Adventure Game! ==== \n") 

# Game Starts Here
print("==========================================================")
print("                      START GAME                          ")
print("==========================================================")

start_keyword = "ENTER"
abort = "Game is aborted due to wrong input. Type ENTER to proceed."

while True:
    # .strip().upper() make "enter", "Enter", or "ENTER " all work
    start_game = input(f"           Type '{start_keyword}' to start the game: ").strip().upper()

    if start_game == start_keyword:
        print("\n \n                     Game started!               \n \n")
        break
    else:
        print(abort)
        print()





# Track if the player is still active/alive in the game
is_alive = True
player_location = "beach"

print("==========================================")
print("LEVEL 1: THE BEACH")
print("==========================================")

if is_alive == True:
    print("You wake up on a beach. You see a dark CAVE, a thick JUNGLE, and an old BOAT.")
    choice1 = input("Where do you want to go? (CAVE / JUNGLE / BOAT): ")
    choice1 = choice1.lower()

    if choice1 == "cave":
        print("You step into the cold, damp cave. A glowing chest sits in the corner.")
        player_location = "cave"
    elif choice1 == "jungle":
        print("You walk into the dense jungle and discover a massive fruit tree.")
        player_location = "jungle"
    elif choice1 == "boat":
        print("You inspect the rotten boat. There is a hole in the bottom, but a radio is inside.")
        player_location = "boat"
    else:
        print("Invalid choice. You sat on the beach too long and got severe sunburn.")
        is_alive = False  # This stops them from proceeding to Level 2



print("==========================================")
print("LEVEL 2: PROGRESSING DEPENDING ON LOCATION")
print("==========================================")


# The game checks if they survived Level 1 before showing Level 2
if is_alive == True:
    print("--- WELCOME TO LEVEL 2 ---")
    
    # Path A: If they went to the Cave
    if player_location == "cave":
        choice2 = input("Do you OPEN the chest or LEAVE the cave? (OPEN / LEAVE): ")
        choice2 = choice2.lower()
        
        if choice2 == "open":
            print("The chest pops open! Inside you find a golden crown and a magical map.")
            player_location = "chest_opened"
        elif choice2 == "leave":
            print("You walk back outside. A massive storm starts brewing overhead.")
            player_location = "beach_storm"
        else:
            print("Invalid choice. You slip in the darkness and fall asleep forever.")
            is_alive = False
        
        
    # Path B: If they went to the Jungle
    elif player_location == "jungle":
        print("You plunge into the thick jungle. The air is humid, and you hear a growl.\n (HIDE / CLIMB)")
        choice2 = "hide"
        
        if choice1 == "hide":
            print("A jaguar was hiding in those bushes. You did not survive.")
            player_location = "riverbank"
        elif choice1 == "climb":
            print("From the treetop, you spot a safe riverbank ahead!")
            is_alive = False
        else:
            print("Invalid choice. You tripped in the dark and fell down a ravine.")
            is_alive = False
        
        
    # Path C: If they went to the Boat
    elif player_location == "boat":
        print("You board the creaking wooden boat. Water starts leaking through the floorboards! \n(ROW / BUCKET)")
        
        choice2 = "row"
        
        if choice2 == "row":
            print("You reach the sandy shores of the island just before the boat sinks!")
            player_location = "island"
        elif choice2 == "bucket":
            print("The leak is too fast! The boat capsizes, and sharks surround you.")
            is_alive = False
        else:
            print("Invalid choice. While you hesitated, the boat filled with water and sank.")
            is_alive = False
        




print("==========================================")
print("LEVEL 3: PROGRESSING TO THE FINALE")
print("==========================================")
# The game checks if they survived Level 2 before showing Level 3
if is_alive == True:
    print("--- WELCOME TO LEVEL 3 ---")
    
    if player_location == "chest_opened":
        choice3 = input("Do you WEAR the crown or follow the MAP? (WEAR / MAP): ")
        choice3 = choice3.lower()
        
        if choice3 == "wear":
            print("The crown turns you into stone. Game Over!")
            is_alive = False
        elif choice3 == "map":
            print("The map guides you to a hidden rescue boat! You escape the island! You win!")
        else:
            print("Invalid choice. A snake bites you while you hesitate. Game Over!")
            is_alive = False
    

# FINAL GAME OVER SCREEN
if is_alive == False:
    print("========================================")
    print("GAME OVER. Better luck next time!")
    print("========================================")
else:
    print("========================================")
    print("CONGRATULATIONS! You survived the island!")
    print("========================================")
