"""
Construct a hierarchy of classes with inheritance. The aim is to construct a Vehicle abstract class. 
This class get 2 parameters from outside via the constructor - brand and year. Use keyword arguments.

Create 2 child classes: Bus and Car . 
There is a common function in these classes that can calculate the fuel consumption
just print out some random value for demonstration purposes.
"""
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def fuel_consumption(self):
        pass

class Car(Vehicle):
    def __init__(self, brand, year):
        super().__init__(brand, year)

    def fuel_consumption(self):
        print('Car fuel consumption')

class Bus(Vehicle):
    def __init__(self, brand, year):
        super().__init__(brand, year)

    def fuel_consumption(self):
        print('Bus fuel consumption')

vehicle_1 = Car('Toyota', 1997)
vehicle_2 = Bus('Mercedez', 2010)

vehicle_1.fuel_consumption()
vehicle_2.fuel_consumption()