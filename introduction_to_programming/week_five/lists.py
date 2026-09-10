#Creating and adding items to a list
items = []

items.append("Wrist watch")
items.append("Mobile Phone")
items.append("Torchlight")

new_item = input("Enter new item: ")
items.append(new_item)

for item in items:
    
    print(item)
