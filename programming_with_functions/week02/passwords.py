"""
Program:                Password Strength Checker

Author:                 Solomon Umoh

Description:            This program let users input password for checking
                        the strength.

Addition:               If an employee's password scores a 2 or less, the program
                        automatically provides helpful suggestions to improve 
                        their password complexity.

"""

LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]


# open and read from the password list file 
def word_in_file(word, filename, case_sensitive=False):
    with open(filename, "r", encoding="utf-8") as file:

        # check for words line by line
        for line in file:
            clean_line = line.strip()

            if case_sensitive:
                if word == clean_line:
                    return True
            else:

                if word.lower() == clean_line.lower():
                    return True
        return False


# draw a line for distinction 
def print_line():
    print("====================================================")


# execute the main function to run the program
def main():
    print("==================== PASSWORD STRENGTH CHECKER ====================\n")

    # loop until user decides to quit
    while True:
        user_password = input("Enter a password to check its strength: ")
        print()

        # if user inputs "q" exit the program
        if user_password.lower() == "q":
            print("Exiting the program.")
            break

        # Display the user inputted password strength
        calculated_strength = password_strength(user_password)

        print_line()
        print(f"The password strength is: {calculated_strength}")
        print_line()

        if calculated_strength <= 2:
            print("Try adding a number or a special symbol to boost security!\n")
            

# check if character is found in word entered by the user
def word_has_character(word, character_list):
    for character in word:
        if character in character_list:
            return True
    return False


# check the complexity of the user inputted password
def word_complexity(word):
    score = 0

    if word_has_character(word, LOWER):
        score += 1

    if word_has_character(word, UPPER):
        score += 1

    if word_has_character(word, DIGITS):
        score += 1

    if word_has_character(word, SPECIAL):
        score += 1 

    return score


# check the strength of the inputted password
def password_strength (password, min_length=10, strong_length=16):
    if word_in_file(password, "wordlist.txt", case_sensitive=False):
        print("Password is a dictionary word and is not secure.")
        return 0

    elif word_in_file(password, "toppasswords.txt", case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0

    elif len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1

    elif len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5

    else:
        complexity = word_complexity(password)
        final_score = 1 + complexity
        return final_score


if __name__ == "__main__":
    main() # execute the program