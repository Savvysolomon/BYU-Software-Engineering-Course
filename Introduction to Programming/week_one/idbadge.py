"""
Program: ID Badge Generator
Author: Solomon Umoh
Programming Language: Python

Description: Program generates ID Badge for users based on the information
            they have inputted and outputs the information to the screen.

"""

print("Please enter the following information:")
print()

first_name = input("First Name: ")
last_name = input("Last Name: ")
email_address = input("Email Address: ")
phone_number = input("Phone Number: ")
job_title = input("Job Title: ")
id_number = input("ID Number: ")

print()
print("The ID Card is:")

print("===============================================")
print(f"{last_name.upper()}, {first_name.capitalize()}")
print(f"{job_title.title()}")
print(f"ID: {id_number}")

print()
print(f"Email: {email_address.lower()}")
print(f"Phone: {phone_number}")

print("===============================================")