men = float(input("How many men are they? "))
women = float(input("How many women are they? "))

total = men + women

if total >= 8 and women >= 4: 
    print("You're are eligible for the game!")

else: 
    print("You're not eligible for the game.")

if not total == 8:
    print("Up for practice.")