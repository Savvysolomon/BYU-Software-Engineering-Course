
color = 'blue'
animal = 'horse'

# You can add, or concatenate, two strings together with +:
print(color + animal)
# This displays: bluehorse

# You can add many strings together, whether the strings are variables or directly in
# the quotation marks:
print(color + ' ' + animal + '!')
# This displays: blue horse!

# You can also save the result into a new string variable:
words_combined = color + " " + animal + "!"
print(f"{words_combined.upper()}")