#LISTS:
#We can create a list using brackets [] and to get and set the elements we use their index
my_list = [1, 4 , 2, 5]

for item in my_list:
    print(item)

my_list[2] = 2.0

for item in my_list:
    print(item)

print(type(my_list))

#to delete an element we use the del operator
del my_list[2]
print(my_list)

#List built-in functions
names_list = ['Oscar', 'Erika', 'Javier', 'Ana']
print(names_list)

#append
names_list.append('Kobe')
print('APPEND')
print(names_list)

#copy
new_names_list = names_list.copy()
print('COPY')
print(names_list)
print(new_names_list)

#extend 
names_list.extend(new_names_list)
print('EXTEND')
print(names_list)


#remove - removes first element that match
names_list.remove('Kobe')
print('REMOVE')
print(names_list)

#pop - removes last element and returns it
print('POP')
print(names_list.pop())

#reverse
names_list.reverse()
print('REVERSE')
print(names_list)

#sort
names_list.sort()
print('SORT')
print(names_list)

#LIST COMPREHENSION
#we can use list comprehension to create new lists
number_list = [number for number in range(1, 11)]
print(number_list)

#we can use conditional statements
squared_even_numbers = [number**2 for number in number_list if number % 2 == 0]
print(squared_even_numbers)

#TUPLES: ITEMS CAN'T BE CHANGED
#LIST [] - TUPLE ()

my_tuple = ('Oscar', 'Erika', 'Javier')

#operations are the same except mutation

#DICTIONARIES
#we have two different ways to create dictionaries
#object literal
my_dict = {'name': 'Oscar', 'age': 24}

#dict() function
my_dict_2 = dict(name='Oscar', age=24)

print(my_dict)
print(my_dict_2)


#keys()
print(my_dict.keys())

#values()
print(my_dict.values())

#items()
print(my_dict.items())

#SETS
#sets are unordered and does not contain duplicates
#object literal
my_set = {'Oscar', 24}

#dict() function
my_set_2 = set(('Oscar', 24))

#transform lists to set
my_set_from_list = set(my_list)
print(my_set_from_list)

#add() add a new item
my_set.add('add()')

#update() add multiple items
my_set.update(['update', 1])

#remove() raise an error if the value is not present in the set
my_set.remove(1)

#discard() does not raise an error
my_set.discard('Does not exists!')

print(my_set)
