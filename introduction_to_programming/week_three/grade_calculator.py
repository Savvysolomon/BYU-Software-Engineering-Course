"""
Program:            Grade Calculator 
Author:             Solomon Umoh

Description:        This program collects grade input from users, figure out the letter grade
                    and display the grade to the user. 

"""

# Ask the student for their grade
grade = float(input("Enter your grade percentage: "))

grade_letter = ""
# Figure out the student's grade letter 
if grade >= 90: 
    grade_letter = "A"
elif grade >= 80:
    grade_letter = "B"
elif grade >= 70:
    grade_letter = "C"
elif grade >= 60: 
    grade_letter = "D"
else:
    grade_letter = "F"


# Get the last digit
last_digit = grade % 10

sign = ""
# Determine the sign
if last_digit >= 7:
    sign = "+"
elif last_digit < 3:
    sign = "-"
else:
    sign = ""


#Handle exceptions (A+, F+, F-)
if grade_letter == "A" and sign == "+":
    sign = "" 
if grade_letter == "F":
    sign = ""


# Display the student's grade letter  
print(f"You have earned the grade: {grade_letter}{sign}.")
print()
print("=================================================")


# Display an appraisal message to the student
if grade >= 70:
    print("Congratulation! You have passed the course!")
else:
    print("Sorry, try the course again.")
print()



x = 6
y = 6

if x == 5:
    print("a")

    if y == 6:
        print("b")
else:
    print("c")

    if y == 10:
        print("d")
