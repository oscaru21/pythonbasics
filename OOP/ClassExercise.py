"""
Construct a class Car with the following features:

create a class variable called color with value black

create 2 instance variables: brand and year

the instance variables are injected from outside - via a constructor

generate functions with which we can acquire the instance variables - these are called getters
"""

class Car:
    color = 'black'

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def get_brand(self):
        return self.brand

    def get_year(self):
        return self.year

toyota = Car('Toyota', 2022)

print(toyota.get_brand())
print(toyota.get_year())