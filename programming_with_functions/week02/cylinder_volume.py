import math

# create the main function that executes every other function
def main():
    # ask the user to input the radius and the height of the cylinder
    radius = float(input("Enter the radius of the cylinder: "))
    height = float(input("Enter the height of the cylinder: "))



    volume = compute_cylinder_volume(radius, height)
    print(f"The volume of the cylinder is: {volume:.2f}")

# NON-REUSABLE FUNCTION WITHOUT PARAMETERS
# def print_cylinder_volume():
#     """compute and print the volume of a cylinder.
#     parameter: none
#     return: nothing
#     """
#     # get the radius and height from the user
#     radius = float(input("Enter the radius of the cylinder: "))
#     height = float(input("Enter the height of the cylinder: "))

#     # compute the volume of the cylinder
#     volume = math.pi * radius ** 2 * height

#     # print the volume of the cylinder
#     print(f"The volume of the cylinder is: {volume:.2f}.")

# print_cylinder_volume()

# NON-REUSABLE FUNCTION WITH PARAMETERS
# def print_cylinder_volume(radius, height):
#     """compute and print the volume of a cylinder.
#     parameter
#     radius: radius of the cylinder 
#     height: height of the cylinder
#     return: nothing
#     """
#     # compute the volume of the cylinder
#     volume = math.pi * radius **2 * height

#     print(f"The volume of the cylinder is: ", volume)

# print_cylinder_volume(50, 20)

def compute_cylinder_volume(radius, height):
    """compute and print the volume of a cylinder.
    parameter
    radius: radius of the cylinder 
    height: height of the cylinder
    return: volume of the cylinder
    """
    # compute the volume of the cylinder
    volume = math.pi * radius ** 2 * height

    # return the volume of the cylinder
    return volume

# start the program by executing the main function
main()