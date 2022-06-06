"""
Construct an application that will open a file with arbitrary text (arbitrary number of lines). 
It reverses the text (not line by line but the whole text) and write this reversed text into another file. 
Let's see an example:

input_file.txt

This is an example
for the input file!
output_file.txt

!elif tupni eht rof
elpmaxe na si sihT
As you can see the lines have been changed as well as the strings have been reversed!
"""

#open files
input_file = open('test.txt', 'r')
output_file = open('output', 'a')

#reverse text
for line in reversed(list(input_file)):
    reversed_line = line[::-1]
    output_file.write(reversed_line)

#close files
input_file.close()
output_file.close()