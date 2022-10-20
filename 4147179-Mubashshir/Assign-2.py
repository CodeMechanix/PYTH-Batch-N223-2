"""
2. Write a Python program to create a function that takes one argument,
and that argument will be multiplied with an unknown given number.
"""
"Solution:"


def get_multiplication(number):
    num2 = int(input("Enter an integer Number: "))
    multiplication = lambda num: num * num2
    return multiplication(number)

num1 = int(input("Enter an integer Number: "))
print("Multiplication:", get_multiplication(num1))