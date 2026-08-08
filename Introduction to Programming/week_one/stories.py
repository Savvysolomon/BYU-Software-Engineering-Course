"""
Program: Story Generator
Author: Solomon Umoh
Programming Language: Python

Description: Program generates a story based on the information
            the user has inputted and outputs the story to the screen.

Addition: The program now includes a more engaging narrative structure with additional details
            and more sentences have been added to the story.

"""

print("Welcome to the story generator program!")

print()
print("Please enter the following:")

print()
adjective = input("Enter a descriptive Adjective: ")
animal = input("Enter an Animal's name: ")  
first_verb = input("Enter an action Verb: ")
exclamation = input("Enter an Exclamation word: ")
second_verb = input("Enter an action Verb: ")
third_verb = input("Enter an action Verb: ")
fourth_verb = input("Enter an action Verb (past tense): ")
repeat_animal = input("Repeat the Animal's name: ") 
fifth_verb = input("Enter an action Verb (past tense): ")



print()
story = (
    f"The other day, I was really in trouble. " 
    f"It all started when I saw a very {adjective} {animal} "
    f"{first_verb} down the hallway. " 
    f"'{exclamation.capitalize()}!' " 
    f"I yelled. But all I could think to do was to {second_verb} over and over. " 
    f"Miraculously, that caused it to stop, but not before it tried to {third_verb}"
    f" right in front of my family. At that moment, I {fourth_verb} my gun " 
    f"and shot it on the head. The {repeat_animal} "
    f"{fifth_verb} and that is how I saved the day."

)

print("Your story is: ")

print()
print("--------------------------------")

print()
print(story)

print()
print("--------------------------------")