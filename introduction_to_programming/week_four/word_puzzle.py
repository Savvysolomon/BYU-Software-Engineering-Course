"""
Program:                Word Puzzle


Author:                 Solomon Umoh


Description:            Word Puzzle is a game that gives players hint to a secret word
                        based on their input.


Addition:               I made it possible for players to keep playing if they enjoy
                        the game by choosing 'yes' or choose 'no' to end the game if
                        they don't enjoy it.

                        Also, the secret words are random choices such that if the player
                        chooses to play again, the secret word changes to a different 
                        one each time.

                        I ensured that the maximum number guess attempt is limited to
                        only 5. Once players exceed the maximum number, game is over.

"""

import random

# Initialize game variables
word_bank = ["program", "develop", "pathway", "puzzler", "players"]

keep_playing = "yes"

while keep_playing == "yes":
    secret_word = random.choice(word_bank)
    word_length = len(secret_word)
    guess_count = 0
    max_guesses = 5
    is_correct = False


# Display welcome message and initial blank hint
    print("=====================================================")
    print()
    print("         Welcome To The Word Guessing Game!        ")
    print()
    print("=====================================================")
    print()

    print(f"======   You have {max_guesses} attempts to get it right.  ======")

    print()
    print("Your hint is: " + " ".join("_" for _ in secret_word))
    print()


    # Main game loop
    while not is_correct and guess_count < max_guesses:
        user_guess = input("What is your guess? ").strip().lower()
        guess_count += 1

        # Validate guess length
        if len(user_guess) != word_length:
            print("Sorry, the guess must have the same number of letters as the secret word.")

        # Calculate the number of guesses left
            guesses_left = max_guesses - guess_count
            print(f"=== Guesses remaining: {guesses_left}. ===")
            print()
            continue


        # Check for a perfect win
        if user_guess == secret_word:
            is_correct = True
        else:
            # Process a valid guess that is wrong, then generate hint
            hint_string = ""
            for i in range(word_length):
                current_letter = user_guess[i]

                if current_letter == secret_word[i]:
                    hint_string += current_letter.upper() + " "
                elif current_letter in secret_word:
                    hint_string += current_letter.lower() + " "
                else:
                    hint_string += "_ "

            print("Your hint is: " + hint_string)
            print()


    # Appraise the player
    if is_correct:
        print("Congratulations! You guessed it right!")
        print(f"It took you {guess_count} guess(es).")
        print()
    else:
        # Maximum guesses exceeded equal to game over
        guesses_left = max_guesses - guess_count
        print(f"Your guess was not correct. Guesses remaining: {guesses_left}")
        print(f"Game Over! The secret word was: {secret_word}.")

    # Ask player if they want to continue playing or quit
    print("=====================================================")
    print()
    keep_playing= input("Would you like to play again (yes / no)? ").strip().lower()
    print()

# Player's response is 'no' end the game
if keep_playing == "no":
        print("Bye! Remember to come back next time.")
