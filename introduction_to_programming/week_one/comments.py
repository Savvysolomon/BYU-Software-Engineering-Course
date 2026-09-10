# Display a greeting 
print("Welcome to the vacation planner program!")

# Gather user input
destination = input("Where are you going for vacation? ")

days =  input("How many days would you like to spend? ")

# Ask for the budget for food and lodging 
print("What is your overall budget for food and lodging?")

# Calculate the lodging cost, food cost and the total price
lodging_cost = 20 #input("Enter your lodging cost: ")
food_cost = 50 #input("Enter your food cost: ")
total_price = (lodging_cost + food_cost)


# Display the itinerary
print(f"Itinerary for the {days} day trip to {destination}.")

print(f"Lodging Cost: {lodging_cost}")
print(f"Food Cost: {food_cost}")
print(f"Your total budget for this vacation is {total_price}")