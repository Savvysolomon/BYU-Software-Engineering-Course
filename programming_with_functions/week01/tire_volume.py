"""

Program:                Tire Volume Calculator


Description:            A program that accepts user input that describes a tire, 
                        then calculate and display the tire's volume. It records 
                        the tire information in a log file.


Addition:               Added a feature that checks the tire size and gives the price 
                        of the tire if it matches a known size. Also, added functionality 
                        to log the phone number of customers who wish to purchase tires.

                        
Author:                 Solomon Umoh

"""

import math 
from datetime import datetime

# print the name of the program
print("===================== TIRE VOLUME CALCULATOR =====================\n")

# print a welcome message
print("Welcome to the Tire Volume Calculator program! Enter valid values to calculate the tire volume.\n")

# prompt the user for input and calculate the volume of the tire
while True:
    tire_width = int(input("Enter the width of the tire in mm (ex 205): "))
    tire_aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
    tire_diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

    # Calculate the volume of the tire using the formula
    volume = (math.pi * tire_width ** 2 * tire_aspect_ratio * (tire_width * tire_aspect_ratio + 2540 * tire_diameter))/10000000000

    # print the approximately calculated volume of the tire
    print("=============================================================")
    print(f"The Approximate Volume of the Tire is: {volume:.2f} liters.")
    print("=============================================================\n")

    # check tire size and give the price
    if tire_width == 185 and tire_aspect_ratio == 50 and tire_diameter == 14:
        price = 80.00
    elif tire_width == 205 and tire_aspect_ratio == 60 and tire_diameter == 15:
        price = 100.00
    elif tire_width == 215 and tire_aspect_ratio == 70 and tire_diameter == 16:
        price = 120.00
    elif tire_width == 225 and tire_aspect_ratio == 80 and tire_diameter == 17:
        price = 140.00
    else:
        price = None

    # print the price of the tire if it matches a known size
    if price is not None:
        print("--------------------------------------------------------------")
        print(f"The Price of the Tire is: ${price:.2f}")
        print("--------------------------------------------------------------\n")
    else:
        print("The price of the tire is not available for the given size.\n")

    # set default value 
    phone_number = "N/A"

    # ask the user they want to buy the tire
    buy_tire = input("Do you want to buy tires with this sizes? (yes/no): ").strip().lower()
    if buy_tire == "yes":
        # prompt the user for their phone number
        phone_number = input("Please enter your phone number: ")
        print()
        print("Thank you for your purchase! Your order has been placed.\n")
    else:
        print("Check out our other tire sizes and prices. We hope to see you again!\n")
        

    # log the tire information in a log file
    with open("volumes.txt", "at") as volumes_file:
        volumes_file.write(f"{datetime.now().strftime('%Y-%m-%d')}, {tire_width}, {tire_aspect_ratio}, {tire_diameter}, {volume:.2f}, {phone_number}\n")

    # ask the user if they want to continue calculating the volume of another tire
    repeat = input("Do you want to calculate the volume of another tire? (yes/no): ").strip().lower()

    # if user does not want to continue, print a thank you message and break the loop
    if repeat != "yes":
        print("Thank you for using the Tire Volume Calculator program! Bye!\n")
        break
