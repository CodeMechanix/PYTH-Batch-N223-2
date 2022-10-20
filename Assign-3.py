"""
3.  Write a Python program to count the even, odd numbers in a given array of integers using Lambda.
"""
"Solution:"


lst = [2, 3, 4, 7, 10, 11, 14, 17, 24, 27, 32]
even_number = list(filter((lambda num: num % 2 == 0), lst))
odd_number = list(filter((lambda num: num % 2 == 1), lst))

print("List of even numbers:\n", even_number)
print("List of odd numbers:\n", odd_number)
even_count = len(even_number)
odd_count = len(odd_number)
print("There are ({}) even number in the list.".format(even_count))
print("There are ({}) odd number in the list.".format(odd_count))