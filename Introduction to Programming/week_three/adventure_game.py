"""
Program:            Adventure Game 
Author:             Solomon Umoh
Description:        The game compels the player to pick an option based on the question 
                    displayed on the screen. Each option picked determines the next message 
                    displayed on the screen.
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
    start_game = input(f"Type '{start_keyword}' to start the game: ").strip().upper()

    if start_game == start_keyword:
        print("Game started! \n \n")
        break
    else:
        print(abort)
        print()
    
print("LEVEL 1 SCENARIO: THE BEACH")
print("...........................................................................")

print(f"You wake up on a beach. You see a dark CAVE, a thick JUNGLE, and an old BOAT.")

first_choice = input("Where do you want to go? (CAVE / JUNGLE / BOAT): ").strip().lower()
print()

# LEVEL 1 BRANCH A: CAVE
if first_choice == "cave":
    print("You step into the cold, damp cave. A glowing chest sits in the corner.")
    print("...........................................................................")

# LEVEL 1 BRANCH B: JUNGLE
elif first_choice == "jungle":
    print("You walk into the dense jungle and discover a massive fruit tree.")
    print("...........................................................................")

# LEVEL 1 BRANCH C: BOAT
elif first_choice == "boat":
    print("You inspect the rotten boat. There is a hole in the bottom, but a radio is inside.")
    print("...........................................................................")    
        
# LEVEL 1 GLOBAL ELSE
else:
    print("Invalid choice. You sat on the beach too long and got severe sunburn. Game Over!\n")


