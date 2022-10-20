"""
2. Write a Python program to create a function that takes one argument,
and that argument will be multiplied with an unknown given number.

"""
# Lambda function
print("-----This is lambda function-----")
mul = lambda num: num * 10
num1 = int(input("Enter a number for multiplication: "))
print("Your result is:", mul(num1))

# Function
print("\n-----This is normal function-----")


def multiplication(num):
    mul = num * 10
    return mul


number = int(input("Enter a number for multiplication: "))
print("Your result is :", multiplication(number))
