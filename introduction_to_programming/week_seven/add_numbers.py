def add(first, second):
    """Purpose: Sum two number and print the result"""
    result = first + second
    return result

num1 = 20
num2 = 40

total = add(num1, num2)
print(f"The sum of num1 and num2 is: {total}")

total = add(num2, num2)
print(f"The sum of num2 and num2 is: {total}")