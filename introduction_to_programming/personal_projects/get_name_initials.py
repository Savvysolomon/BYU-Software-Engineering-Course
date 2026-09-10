# importing from library
from datetime import datetime

# < ======= Function defination starts here

# function for getting name initials
def get_initials(name):
    initial = name[0:1].upper()
    return initial

# function for printing present date and time 
def print_time():
    print(datetime.now())

# function for printing line 
def print_line():
    print("=============================================")

# Function defination ends here ============== >


# < ========= main code section starts here ===================

# ask user for their first name and store the initial in a variable
first_name = input("Enter your first name: ")
get_first_initial = get_initials(first_name)

# ask user for their last name and store the initial in a variable
last_name = input("Enter your last name: ")
get_last_initial = get_initials(last_name)

# print the two initials to the screen
print_line()
print(f"Your initials are: {get_first_initial}.{get_last_initial}.")

print_line()

# print additional information like date and time
print('Printed in the year and at the time below:')
print_time()

# ============ main code section ends here ============= >
