"""
Construct a function that has 1 parameter - the x variable. If x is smaller than 0 then return with 0. 
Otherwise return with +1. (Note: there may be multiple return statements in a given function)
"""

def my_function(x):
    if x < 0:
        return 0
    else:
        return 1

print(my_function(-1))
print(my_function(1))

