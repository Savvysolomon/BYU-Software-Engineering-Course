def get_message(message):

    print(f"{message}")
    print(f"{message.lower()}")
    print(f"{message.upper()}")

user_message = get_message(input("What is your message? "))

get_message(user_message)


