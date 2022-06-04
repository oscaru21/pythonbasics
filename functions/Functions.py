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