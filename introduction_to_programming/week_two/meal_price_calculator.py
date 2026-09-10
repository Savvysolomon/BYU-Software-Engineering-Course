"""
Program:        Meal Price Calculator

Description:    This program calculates the subtotal, sales tax, total cost of a meal 
                for children and adults and the change due based on user input.

Author:         Solomon Umoh


Addition:       Drinks are included in the meal price. The user will be prompted 
                to enter the price of a child's meal, the price of a child's drink, 
                the price of an adult's meal, and the price of an adult's drink. 
                        

"""


# Ask for the price of a Child's and Adult's Meal and Drink
child_meal_price = float(input("What is the price of a child's meal? "))
child_drink_price = float(input("What is the price of a child's drink? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))
adult_drink_price = float(input("What is the price of an adult's drink? "))


# Ask for the number of Children and Adults
children_number = int(input("How many children are there? "))
adult_number = int(input("How many adults are there? "))

#Determine the meal's subtotal for Children and Adults
children_meal_total = children_number * child_meal_price 
children_drink_total = children_number * child_drink_price
adult_meal_total = adult_number * adult_meal_price 
adult_drink_total = adult_number * adult_drink_price


# ============== Subtotal for both Adults and Children ====================
subtotal = children_meal_total + children_drink_total + adult_meal_total + adult_drink_total

print()
print("=============================================")
print(f"Subtotal: ${subtotal:.2f}")
print("=============================================")


# ===============================================================
print()
#Ask the user for the sales tax rate as a percentage
sales_tax_rate = float(input("What is the sales tax rate (as a percentage)? "))

#Compute the sales tax
compute_sales_tax = subtotal * (sales_tax_rate / 100)

print(f"Sales Tax: ${compute_sales_tax:.2f}")



#Compute the total cost of the meal
compute_total = subtotal + compute_sales_tax

print()
print("=============================================")
print(f"Total:  ${compute_total:.2f}")
print("=============================================")

print()
#Ask the user for the the payment amount 
payment_amount = float(input("What is the payment amount? "))

#Compute the customer's change due
change_due = payment_amount - compute_total

print("=============================================")
print(f"Change Due: ${change_due:.2f}")
print("=============================================")

print()
print(" Thank you for patronizing us. Have a great day!")
