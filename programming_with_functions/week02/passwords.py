"""
Program:                Password Strength Checker

Author:                 Solomon Umoh

Description:            This program let users input password for checking
                        the strength.

"""

# open and read from the password list file 
def word_in_file(word, filename, case_sensitive=False):
    pass

# execute the main function to run the program
def main():
    # loop until user decides to quit
    while True:
        user_password = input("Enter a password to check its strength: ")

        # if user inputs "q" exit the program
        if user_password.lower() == "q":
            print("Exiting the program.")
            break

        # display the user inputted password
        password_strength(user_password)

# check word character
def word_has_character(word, character_list):
    pass

# check the complexity of the user inputted password
def word_complexity(word):
    pass

# check the strength of the inputted password
def password_strength (password, min_length=10, strong_length=16):
    print(f"Password entered: {password}")

main() # execute the program