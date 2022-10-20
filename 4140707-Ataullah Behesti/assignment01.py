# 1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,

add = lambda num : num +15
print(add(10))

# also create a lambda function that multiplies argument x with argument y and print the result.

multiply = lambda x,y : x * y
x = int(input("Enter x:"))
y = int(input("Enter y:"))
print(f"Multiplication =",multiply(x,y))