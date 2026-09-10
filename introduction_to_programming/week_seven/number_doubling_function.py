def get_double(value):
    double_value = value * 2

    return double_value

stop = "quit"

while user_input := get_double(float(input("Enter a number to double: "))):
    print(user_input)
        


