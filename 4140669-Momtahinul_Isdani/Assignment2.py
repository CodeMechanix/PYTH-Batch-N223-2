"""
2. Write a Python program to create a function that takes one argument,
and that argument will be multiplied with an unknown given number.
"""


def get_multiplication(number):
    return number * 4


num1 = int(input("Enter an Integer Number: "))
print("Multiplication:", get_multiplication(num1))
