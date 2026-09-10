# Products available on the shelf
shelf = {
    "apple": {"display_name": "Apple", "price": 100},
    "orange": {"display_name": "Orange", "price": 50},
    "carrot": {"display_name": "Carrot", "price": 150}
}

tax_rate = 0.05
shopping_cart = []  # List to store the items the user chooses

print("==================================================")
print("There are 3 products on the shelf:")
for item in shelf.values():
    print(f"- {item['display_name']}: ${item['price']}")
print("==================================================")
print("Type 'checkout' when you are done shopping.")
print("==================================================\n")

# Loop 1: Shopping Phase
while True:
    user_choice = input("Enter a product to buy (or 'checkout' to finish): ").strip().lower()
    
    if user_choice == 'checkout':
        if not shopping_cart:
            print("Your cart is empty. Please add at least one item before checking out.\n")
            continue
        break  # Exit the loop and go to payment
        
    if user_choice not in shelf:
        print("Product is not on the shelf. Check again.\n")
    else:
        # Add the chosen product dictionary to the cart
        shopping_cart.append(shelf[user_choice])
        print(f"Added {shelf[user_choice]['display_name']} to your cart.\n")

# Calculate total price of all items in the cart
product_sum = sum(item['price'] for item in shopping_cart)
calculated_tax = product_sum * tax_rate
total_bill = product_sum + calculated_tax

print()
print("==================================================")
print("YOUR RECEIPT:")
for item in shopping_cart:
    print(f"- {item['display_name']}: ${item['price']}")
print(f"Subtotal: ${product_sum:.2f}")
print(f"Tax (5%): ${calculated_tax:.2f}")
print(f"Total Amount Due: ${total_bill:.2f}")
print("==================================================")
print()

# Loop 2: Payment Phase
while True:
    payment = float(input("What is the payment amount? "))

    if payment < 0:
        print("Sorry, the payment amount cannot be negative.\n")
        continue
    elif payment < total_bill:
        print(f"Not enough money. Your total bill is ${total_bill:.2f}.\n")
        continue
    else:
        print("Correct value inputted.")
        print()
        print("===================================================")
        print(f"Payment amount received: ${payment:.2f}.")
        print("===================================================")

    change = payment - total_bill
    
    print(f"Change returned: ${change:.2f}")
    print()
    print("Thank you for patronizing us!")
    print("===================================================")
    break
