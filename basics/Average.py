"""
Construct an application that calculates the average of the first 10 items - starting with 1. 
So [1,2,3,4,5,6,7,8,9,10] these are the numbers you have to consider - with loops of course :)
"""

arr = [1,2,3,4,5,6,7,8,9,10]
sum = 0

for number in arr:
    sum += number
else:
    avrg = sum / len(arr)
    print(avrg)