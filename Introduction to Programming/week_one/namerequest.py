"""
Program: Name Request
Author: Solomon Umoh
Programming Language: Python

Description: Program asks for the last and first name of the user, stores the names in 
            a variable and outputs the names to the screen accordingly.

"""
# This is lines are for requesting the first and last name of the user and storing them in a variable.
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

#This line outputs the first and last name of the user to the screen ensuring that the first letter of each name is capitalized.
print(f"Your name is {last_name.title()}, {first_name.title()} {last_name.title()}.")