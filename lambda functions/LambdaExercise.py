"""
We have 2 list data structures - one with names and another with integers.

names = ['Adam', 'Kevin', 'Joe']
nums = [1, 2, 1]

Construct an algorithm that takes the names one by one and multiply them by the integers 
integers with the same index in the other array. Make sure you capitalize the letters of the names.
"""
names = ['Adam', 'Kevin', 'Joe']
nums = [1, 2, 1]

result = list(map(lambda name, num : str.upper(name)*num, names, nums))
print(result)