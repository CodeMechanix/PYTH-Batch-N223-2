"""
2. Write a Python program to create a function that takes one argument,
and that argument will be multiplied with an unknown given number.
"""


def multiplication(num):
    number1 = int(input("Enter another number for multiplication: "))
    mul = lambda num: num * number1
    return mul(num)


number = int(input("Enter a number for multiplication: "))
print("Your result is :", multiplication(number))
