#classes are the blueprints for objects
class Animal:
    #class variables
    total_animals = 0
    #we can create something similar to a private variable using __ like this
    #in reality Python is just changin the name to _Animal__color
    __color = 'black'

    #__init__ is the constructor and it takes a reference to the instance as the first argument
    def __init__(self, name):
        #instance variables
        self.name = name

        Animal.total_animals += 1

    #we can define methods as functions inside the class
    def show_name(self):
        print("I'm a " + self.name)

#We can create an intance of a class just by calling its name
my_animal = Animal('Dog')
my_animal_2 = Animal('Cat')

my_animal.show_name()

print(my_animal.total_animals)
print(my_animal_2.total_animals)

##class inheritance

#Parent class - the more abstract class
class Vehicle:
    #class variable
    message = 'This is a Vehicle'

#Child class - it contains more specific characteristics or behavior
#to extend the parent class we pass it as an argument
class Car(Vehicle):
    #class variable
    sound = 'Honk Honk'

#If we instatiate a new child class object we can access all of the child and parent class variables
nissan = Car()
print(nissan.sound)
print(nissan.message)

#super() keyword
#the super keyword makes reference to the parent class
class User:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def show_user(self):
        print('Hi my name is %s and Im a %s' % (self.name, self.gender))

class FacebookUser(User):
    def __init__(self, name, age):
        super().__init__(name, age)


facebook_user = FacebookUser('Oscar', 'Man')
facebook_user.show_user()