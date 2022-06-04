"""
Construct an application that prints the first 9 Fibonacci-number with the help of a for loop!
"""

a, b = 0, 1

for el in range(9):
    print(a)
    a, b = b, a+b