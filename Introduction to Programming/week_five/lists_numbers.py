# Creating list of numbers

points_scored = [24, 18, 31, 42, 28]

total_score = 0

for points_number in points_scored:
    total_score += points_number
    print(points_number)
print(f"The player scored a total of {total_score} points.")