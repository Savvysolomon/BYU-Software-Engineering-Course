"""

Program:                Shopping Cart

Author:                 Solomon Umoh


Description:            A program that stores a list of products in a shopping cart 
                        along with their prices. The program allows users to  add items 
                        to the list, remove them, and see the total price of the cart.

                        
Addition:               1. Quantity is added to the program
                        2. Print receipt option added to the program
                        3. Receipt properly indented
                        4. Cart empty message is added to view cart option
                        5. Cannot print receipt for empty cart message added

"""

# Initialize the variables
item_names = []
item_prices = []
item_quantities = []

business_feedback = "Thank you for patronizing Shopping Cart Enterprises!"

# Welcome customers to the shop
print("================== Shopping Cart Enterprises! ================")
print()
print("==============================================================")

print(" You are warmly Welcomed. Add your desired item to the cart!")

print("==============================================================")
print()

# Loop menu list until correct option is selected
while True:
    print("Please select one of the following:")
    print("1. Add item") 
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Print receipt")
    print("6. Quit")

    print()
    # Ask user to select an option
    user_action = input("Please enter an action:").strip()


    # Add item to the cart
    if user_action == "1":
            item = input("What item would you like to add? ").strip()
            item_names.append(item.capitalize())

            quantity = int(input(f"How many {item} would you like to add? "))
            item_quantities.append(quantity)

            price = float(input(f"What is the price of {item}? "))
            item_prices.append(price)

            print("------------------------------------------------")
            print(f"'{item}' (x{quantity}) has been added to the cart.")
            print()


    # Display content of the cart
    elif user_action == "2":
        if len(item_names) == 0:

            print("------------------------------------------------")
            print("Your shopping cart is empty.")
            print()
        else:

            print("The contents of the shopping cart are:")
            for i in range(len(item_names)):
                print(f"{i + 1}. {item_names[i]} (Qty: {item_quantities[i]}) - ${item_prices[i]:.2f} each")
            
                print("------------------------------------------------")

    # Remove item from cart
    elif user_action == "3":
        print("The contents of the shopping cart are:")
        for i in range(len(item_names)):
            print(f"{i + 1}. {item_names[i]} (Qty: {item_quantities[i]}) - ${item_prices[i]:.2f} each")

        print()
        user_choice = int(input("What item would you like to remove? "))
        
        target_index = user_choice - 1
        if target_index >= 0 and target_index < len(item_names):
            item_names.pop(target_index)
            item_prices.pop(target_index)
            item_quantities.pop(target_index)

            print("------------------------------------------------")
            print("The selected Item has been removed from the cart.\n")
        else:
            print("------------------------------------------------")
            print("Sorry, that is not a valid item number. \n")
            

    # Compute the total price of items
    elif user_action == "4":
        total_price = 0

        for i in range(len(item_names)):
            total_price += item_prices[i] * item_quantities[i]

        print("------------------------------------------------")
        print(f"Total price of items in cart is: ${total_price:.2f}")
        print("------------------------------------------------")


    # Print receipt for customer
    elif user_action == "5":
        if len(item_names) == 0:
            print("Cannot print a receipt for an empty cart.")
            print()
        else:

            print("\n================== RECEIPT ===================== \n")
            

            print(f"- {'Item':<15} {'Quantity':<15} ... {'Amount'}")
            print("------------------------------------------------")
            
            total_price = 0
            for i in range(len(item_names)):

                item_subtotal = item_prices[i] * item_quantities[i]

                total_price += item_subtotal
                print(f"- {item_names[i]:<15} {item_quantities[i]:<15} ... ${item_subtotal:.2f}")

            print("------------------------------------------------")

            grand_total = total_price        
            print(f"GRAND TOTAL:                      ... ${grand_total:.2f}")

            print("================================================\n")

            print(f"{business_feedback} \n")


    # Quit the program
    elif user_action == "6":
        print("Thank you. Goodbye.")
        print()
        break

    else:
        print("Invalid selection. Please choose a number between 1 and 6.")



