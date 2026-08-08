# Import the random library
import random

#Assign entry point of the loop
keep_playing = "yes"

while keep_playing == "yes":
    secret_number = random.randint(1, 100)

    guess_number = ""

    guess_count = 0

    while guess_number != secret_number:
        guess_number = int(input("What is your guess? "))

#Increment the guess count per input
        guess_count += 1

# Set the criteria to be met
        if guess_number < secret_number:
            print("Higher")
        elif guess_number > secret_number:
            print("Lower")
        else:
            print("You guessed right!")


#Print the output
    if guess_count == 1:
        print(f"It took you {guess_count} guess.")
    else:
        print(f"It took you {guess_count} guesses.")

#Ask if user enjoys the game and wants to continue
    keep_playing = input("Would you like to play again (yes / no)? ")