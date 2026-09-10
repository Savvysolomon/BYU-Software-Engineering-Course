def get_positive_value(prompt_text):
    """Ask users for a positive number and return the value,
    reprompt the user if the value is negative.
    """
    value = float(input(prompt_text))

    # return the value
    return value

length = get_positive_value("Enter the length of the rectangle: ")

while length < 0:    
    print("Sorry, the length cannot be negative.")
    length = get_positive_value("Enter the length of the rectangle: ")


width = get_positive_value("Enter the width of the rectangle: ")

while width < 0:     
    print("Sorry, the width cannot be negative.")
    width = get_positive_value("Enter the width of the rectangle: ")
    
area = length * width

print(area)