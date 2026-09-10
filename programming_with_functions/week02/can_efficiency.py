import math

# create a main function that calls other functions
def main():
    name = "#1 Picnic"
    radius = 6.83
    height = 10.16
    volume = can_vol(radius, height)
    surface_area = can_surface_area(radius, height)
    efficiency = storage_efficiency(volume, surface_area)
    print(f"Name: {name} | Volume: {volume:.2f} | Surface Area: {surface_area:.2f} | Efficiency: {efficiency:.2f}\n")


    can_efficiency("#1 Tall", 7.78, 11.91)

    can_efficiency("#2", 8.73, 11.59)

    can_efficiency("#2.5", 10.32, 11.91)

    can_efficiency("#3 Cylinder", 10.79, 17.78)

    can_efficiency("#5", 13.02, 14.29)

    can_efficiency("#6Z", 5.40, 8.89)

    can_efficiency("#8Z short", 6.83, 7.62)

    can_efficiency("#10", 15.72, 17.78)

    can_efficiency("#211", 6.83, 12.38)

    can_efficiency("#300", 7.62, 11.27)

    can_efficiency("#303", 8.10, 11.11)


# create a function to calculate volume of a can
def can_vol(radius, height):
    volume = math.pi * radius ** 2 * height
    return volume

# create a function to calculate surface area of a can
def can_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

# create a function to calculate storage efficiency of a can
def storage_efficiency(volume, surface_area):
    efficiency = volume / surface_area
    return efficiency


def can_efficiency(name, radius, height):
    volume = can_vol(radius, height)
    surface_area = can_surface_area(radius, height)
    efficiency = storage_efficiency(volume, surface_area)
    print(f"Name: {name} | Volume: {volume:.2f} | Surface Area: {surface_area:.2f} | Efficiency: {efficiency:.2f}\n")

main() # call the main function to execute the program