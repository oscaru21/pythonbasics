"""
Construct a recursive function that takes 2 parameters as input - a string and a given index ( of the text). 
The aim is to visit every character of the text (from left to right - so starting with index 0) recursively.
"""

def recursive_traversion(text, i):
    #base case
    if i == len(text):
        return 
    
    print(text[i])
    recursive_traversion(text, i+1)

recursive_traversion('Oscar Rodolfo', 5)