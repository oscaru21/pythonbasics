"""
There are 5 different basic data types in python programming language
1)number
2)string
3)list
4)tuple
5)dictionary
"""
#NUMBERS:
#a variable is declared as soon as we assign a value 
num1 = 10
print(num1, type(num1))

#we can do multiple variable declaration in a single line sing commas
num2, num3 = 5.3, 10
print(num2, type(num2))
print(num3, type(num3))

#python understands the type of each number and is capable of perform operations
f = 1.0
integer = 3
print(f + integer)

#BOOLEANS
#booleans are binary values the are written with the first capital letter
true = True
false = False
print(true, type(true))
print(false, type(false))

#booleans are the result of comparison operations
equal = True == False
greater_than = True > False
less_than = True < False
not_equal = True != False
print(equal, greater_than, less_than, not_equal)
print( 1 == True)

#STRINGS:
string = 'Hi this is a string'
print(string, type(string))

#string in python are one dimensional arrays
#that means that we can use all the array methods and sintax like use range notation to get substring
print(string[0])
print(string[-1])
print(string[:])

#the range operator includes the first argument but not the second
print(string[3:7])

#to concatenate strings with numbers we can use the format method that works similar to the template string in js
text = 'This is a template with the number {} and a second number {}'
print(text.format(15, 16))

#the : operator also let us define the step value which can be positive or negative
#positive means from left to right
#negative means from right to left
palindrome = 'I did, did I'
print('normal string: ' + palindrome[:])
print('reversed string: ' + palindrome[::-1])

#TYPE CASTING: python is an OOP language and sometimes is necessary to force an specific type
a = 1
b = '1'
c = True
template = 'a: {} type: {}, b: {} type: {}, c: {} type: {}'
print(template.format(a, type(a), b, type(b), c, type(c)))

#casting floats
a = float(1)
b = float('1')
c = float(True)
print('floats:')
print(template.format(a, type(a), b, type(b), c, type(c)))

#casting integers
a = int(1)
b = int('1')
c = int(True)
print('integers:')
print(template.format(a, type(a), b, type(b), c, type(c)))

#casting strings
a = str(1)
b = str('1')
c = str(True)
print('strings:')
print(template.format(a, type(a), b, type(b), c, type(c)))

#LOOPs
#FOR LOOPS: for loops needs an iterator, it can be a range, an Array or a string
print('for loop with range:')
for number in range (10, 5, -1):
    print(number)

print('for loop with array:')
arr = [1, 2, 3, 4, 5]
for number in arr:
    print(number)

print('for loop with string:')
string = 'Oscar!'
for char in string:
    print(char)


#ENUMERATE: it return the index and the value of an array
values = ['erika', 'javier', 'oscar']
for index, val in enumerate(values):
    print(index, val)