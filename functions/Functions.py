#FUNCTIONS
#We can define functions in python using the def keyword

def my_first_function(name):
    print('Hi, my name is {}'.format(name))

#we can use the pass keyword to define an empty function

def empty_function(param):
    pass

my_first_function('Oscar')
empty_function('Oscar')

#POsitional arguments
#when we define a function we assign a name to and a position to the arguments
#if we invoke the function without the argument names is going to assign the value depending on the position
def position_function(arg1, arg2):
    print(arg1)
    print(arg2)

position_function('arg1', 'arg2')
position_function('arg2', 'arg1')

#undefined number of args
#if we dont know the number of argument we can use an * to define a tuple of values 
def multiple_position_function(*args):
    for item in range(len(args)):
        print(item)

#Keyword arguments
#if we invoke the function with the argument names is going to assign the value depending on the name
def keyword_function(arg1, arg2):
    print(arg1)
    print(arg2)

keyword_function(arg1='arg2', arg2='arg1')


#Undefined number of kwargs
#if we dont know the number of argument we can use an ** to define a dictionary of key-value pairs
def multiple_keyword_function(**kwargs):
    print(kwargs['name'])
    print(kwargs['age'])

multiple_keyword_function(age=24, name='Oscar')

#RETURNING MULTIPLE VALUES
#In python we can return multiple values as a tuple and we can destructure the result when we call the function
def division(dividend, divisor):
    quotient = dividend//divisor
    remainder = dividend%divisor
    return quotient, remainder

q, r = division(20, 3)
result = division(20, 3)

print(type(result))
print(q)
print(r)

#GLOBAL and LOCAL variables

#global variable
NUMBER = 10

def local_global_function():
    #local variables
    NUMBER = 15
    #does the print functions print the local or the global variable or throws and error?
    print(NUMBER)
    #A/ it prints the local and ignores the global

#it print the global
print(NUMBER)
local_global_function()

#MOST RELEVANT BUILD-IN FUNCTIONS
#print()
#int()
#type()
#str()
#range()
#pow() - more efficient than **

#RECURSION
#It's a given function that calls itself
#whe must have a base case that will stop the recursion
#and a recursive call

def sum_recursion(n):
    #base case n = 0
    if n == 0:
        return 0
    else:
        return n + sum_recursion(n-1)

print(sum_recursion(6))

#factorial: n! = n * (n-1)! and 1! = 1
def factorial(n):
    #base case
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))