"""
Create a Python application that process an input from the user. 
The input is an integer and you have to check the following:

if the given integer is smaller than 0: 
    then show a message to the user that the given integer is smaller than zero

if the given integer is greater than (or equal to) 0 and smaller than (or equal to) 10: 
    then show a message to the user that the given integer is within the range [0,10]

if the given integer is greater than 10: 
    show a message to the user that the integer is greater than 10
"""

num = int(input('Please enter an integer: '))

if num < 0:
    print('The given integer is smaller than zero')
elif num >= 0 and num <= 10:
    print('The given integer is within the range [0,10]')
else:
    print('The integer is greater than 10')