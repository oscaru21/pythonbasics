"""
Construct a dictionary (with key and value pairs) out of 2 lists.

These are the values in the names and ages lists accordingly. 
The aim is to end up with a single dictionary data structure with the names (as keys) 
and the ages (as the values accordingly).
"""

names = ['Adam', 'Daniel', 'Ana']
ages = [34, 12, 54]

def create_dictionary(keys, values):
    my_dict = {}

    for key, value in zip(keys, values):
        my_dict[key] = value
    
    return my_dict

print(create_dictionary(names, ages))