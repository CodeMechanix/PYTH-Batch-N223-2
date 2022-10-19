"""
3.  Write a Python program to count the even, odd numbers in a given array of integers using Lambda.
"""

lst = list(map(int, input("Enter Integer numbers separated by space: ").split()))

# using lambda filter
print("# using lambda filter")
evenCount = len(list(filter(lambda num: (num % 2 == 0), lst)))
oddCount = len(list(filter(lambda num: (num % 2 == 1), lst)))
print("Total Even: ", evenCount, "\nTotal Odd: ", oddCount)


# using comprehension
print("# using comprehension")
evenCount = len([num for num in lst if num % 2 == 0])
oddCount = len([num for num in lst if num % 2 == 1])
print("Total Even: ", evenCount, "\nTotal Odd: ", oddCount)
