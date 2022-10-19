"""
1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
also create a lambda function that multiplies argument x with argument y and print the result.
"""
# Summation
sum = lambda num: num + 15
user_input_to_add = int(input("Enter a number: "))
print("Your result is:",sum(user_input_to_add))

# Multiplication
mul = lambda x, y: x * y
x, y = map(int, (input("Enter 2 number with a space: ").split()))
print("Multiplication of your given number is:", mul(x, y))
