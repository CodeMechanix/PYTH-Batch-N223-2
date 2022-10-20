"""
1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
also create a lambda function that multiplies argument x with argument y and print the result.
"""
print("\n===========Addition==========")
get_addition = lambda num: num + 15
num1 = int(input("Enter an Integer Number: "))
print(f"Addition: {num1} + 15 =", get_addition(num1))

print("\n==================================\n")
print("==========Multiplication==========")
get_multiplication = lambda x, y: x * y
num2 = int(input("Enter value of X: "))
num3 = int(input("Enter value of Y: "))
print(f"Multiplication: {num2} X {num3} =", get_multiplication(num2, num3))

