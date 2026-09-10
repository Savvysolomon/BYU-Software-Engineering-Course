# Square 
# Ask for the information 
side = float(input("What is the length of the side of the square? "))

# Calculate the area of a square
square_area = side * side


# Display the result
print(f"The area of the square is: {square_area}")

# Rectangle
# Ask for the rectangle's length and width
length = float(input("What is the length of the rectangle? "))
width = float(input("What is the width of the rectangle? "))

#Calculate the area of a rectangle
rectangle_area = length * width

# Display the resulting area
print(f"The area of the rectangle is: {rectangle_area}")


# Circle
# Ask for the radius of the circle
radius = float(input("What is the radius of the circle? "))

# Calculate the area of a circle
circle_area = 3.14 * radius * radius

# Display the resulting area of the circle
print(f"The area of the circle is: {circle_area}")


#=========================================================================================


print()
print("========================================================================================")
print("The part below is for calculating the areas in square centimeters and square meters.")
print("========================================================================================")

print()
# Square 
# Ask for the information 
side = float(input("What is the length of the side of the square (in cm)? "))

# Calculate the area of a square
square_area_cm2 = side * side
square_area_m2 = square_area_cm2 / 10000

# Display the result
print(f"The area of the square is: {square_area_cm2} cm^2")
print(f"The area of the square is: {square_area_m2} m^2.")

# Rectangle
# Ask for the rectangle's length and width
length = float(input("What is the length of the rectangle (in cm)? "))
width = float(input("What is the width of the rectangle (in cm)? "))

#Calculate the area of a rectangle
rectangle_area_cm2 = length * width
rectangle_area_m2 = rectangle_area_cm2 / 10000

# Display the resulting area
print(f"The area of the rectangle is: {rectangle_area_cm2} cm^2")
print(f"The area of the rectangle is: {rectangle_area_m2} m^2.")


# Circle
# Ask for the radius of the circle
radius = float(input("What is the radius of the circle (in cm)? "))

# Calculate the area of a circle
circle_area_cm2 = 3.14 * radius * radius
circle_area_m2 = circle_area_cm2 / 10000

# Display the resulting area of the circle
print(f"The area of the circle is: {circle_area_cm2} cm^2")
print(f"The area of the circle is: {circle_area_m2} m^2.")

