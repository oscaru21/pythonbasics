#in order to define a lambda expression we need to follow this structure
# lambda 'bound variable' : 'body of lambda expression'


number = lambda x: x + 1

#We can combine regular functions with lambda functions in order to create functions more dinamicly
#for example if we think about multiplication or exponentiation they have constant values so we could declare a function that returns another function


def multiply(factor):
    return lambda x: factor * x


#now we can create specific functions
int_double = multiply(2)
int_triple = multiply(3)

print(int_triple(10))
print(int_double(10))

#FILTER function

#lets create a list of number from 1 to 100
nums = [num for num in range(1, 101)]

#now lets use the filter function to get the even numbers
even_nums = list(filter(lambda num: num % 2 == 0, nums))
print(even_nums)

#lets create a list of dictionaries
users = [{
    "name": "Oscar",
    "age": 24
}, {
    "name": "Erika",
    "age": 28
}, {
    "name": "Javier",
    "age": 25
}, {
    "name": "Pepe",
    "age": 15
}]

#lets filter user depending on the age
legal_age_users = list(filter(lambda user: user['age'] > 24, users))
print(legal_age_users)

#MAP function
#map functions allow us to transform a list

uppercase_users = list(map(lambda user : {**user, 'name': str.upper(user['name'])}, users))

print(uppercase_users)
