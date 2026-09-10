# Initialize Variables
number = []

user_number = -1


# Ask user for number
while user_number != 0:
    user_number = int(input("Enter the number: "))



    if user_number != 0:
        #Append the numbers to the list
        number.append(user_number)

print(number)