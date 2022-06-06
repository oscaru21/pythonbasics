
#we can open a file using the open() we need to pass the name of the file and the action 
#r - read
#w - write
#a - append

file = open('test.txt', 'r')

#we can read the file line by line
#for line in file:
#    print(line)

#we can process the file character by character
while True:
    actual_char = file.read(1)

    if not actual_char:
        break

    print(actual_char)

print(type(file))

file.close()