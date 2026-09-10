"""
Program:        Number Summation

Description:    A program that adds numbers based on user input

Author:         Solomon Umoh

"""

# define the sum function
def add_amount():
     result =  first_user_input + second_user_input
     return result


print("================================ Welcome to Summation ================================\n")

# ask for user input 
while True:
     first_user_input = float(input("Enter the first amount: "))
     print(f"First Amount: ${first_user_input}\n")
     second_user_input = float(input("Enter the second amount: "))
     print(f"Second Amount: ${second_user_input}\n")


# print the result 
     print("===============================================")
     print(f"The sum of the inputted amounts is: ${add_amount()}")
     print("===============================================\n")


