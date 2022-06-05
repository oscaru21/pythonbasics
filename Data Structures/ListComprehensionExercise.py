"""
The aim is to filter an exiting list of integers with the list comprehension approach. 
So here is a function that determines whether an input is prime or not:
"""
def is_prime(x):
 
    if x < 0:
        return False
    if x == 1:
        return False
    if x == 2:
        return True
 
    for num in range(2, x):
        if x % num == 0:
            return False
 
    return True 

numbers = [1, 5, 43, 55, 76, 100, 123, 11, 2, -5, 87, 99]
"""
a.)

Write an algorithm that filters this list of integers and constructs a new list with the prime numbers. 
Of course you can use the is_prime() function to decide whether an integer is prime or not.
"""

prime_numbers_list = [number for number in numbers if is_prime(number)]
print(prime_numbers_list)

"""
b.)

Create a list of squared values in the range [5, 10] - 5 and 10 are part of the interval. 
So the result should be [25, 36, 49, 64, 81, 100]. Use list comprehension!
"""

squared_numbers_list = [pow(number, 2) for number in range(5, 11)]
print(squared_numbers_list)