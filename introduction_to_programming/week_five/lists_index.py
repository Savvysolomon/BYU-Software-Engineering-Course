# Index =   0        1       2         3
colors = ["Red", "Green", "Blue", "Yellow"]

# user_input = ""

while user_input != "quit":
    user_input = input("Add item to the list: ")
    if user_input != "quit":
        colors.append(user_input.capitalize())

    # print("======== Items In The List Are: =========")
    # # print(colors)
    # print("=========================================")

    # print("======== Items In The List Are: =========")
    # colors.insert(0, "Orange")

    # colors.remove("Yellow")


    # print(colors[1])


# for color in colors:
#     print(color)

# colors.pop(0)

#     for i in range(len(colors)):
#             color = colors[i]
#             user_input = i + 1

#     print(f"{user_input} - {color}")
#     print("=========================================")
#     print()

# print(colors)



