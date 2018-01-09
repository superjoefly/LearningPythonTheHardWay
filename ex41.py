# Exercise 41: Learning Object Oriented Language
#
# Practice using oop_test.py


# # Exercise 42: Is-A, Has-A, Objects and Classes
#
# A class inherits from the class named 'object' to make a class, but, it's not an object...really it's a class, but don't forget to inherit from object
#
# # Python always requires (object) when you make a class




# # Animal is-a object (yes, sort of confusing) look at the extra credit
# class Animal(object):
#     pass
#
# # Make a class Dog that is-a animal
# class Dog(Animal):
#     def __init__(self, name, fur_color, sound):
#
#         self.name = name
#         self.fur_color = fur_color
#         self.sound = sound
#
#     def make_sound(self):
#         print "The dog say's", self.sound
#
# rover = Dog('Rover', 'black', 'bark!')
# print rover.name
# print rover.fur_color
# print rover.sound
# print rover.make_sound()
#
# # Make a class Cat that is-a Animal
# class Cat(Animal):
#     def __init__(self, name, fur_color, sound):
#
#         self.name = name
#         self.fur_color = fur_color
#         self.sound = sound
#
#     def make_sound(self):
#         print "The cat say's", self.sound
#
# kitty = Cat('Kitty', 'orange', 'meow!')
# print kitty.name
# print kitty.fur_color
# print kitty.sound
# print kitty.make_sound()




# # Class Person is-a object
# class Person(object):
#     def __init__(self, name):
#         # Class Person has-a name
#         self.name = name
#         # Class Person has a pet (of some kind)
#         self.pet = None # set to a default of None
#
#
# # Make a Class Employee that is-a Person
# class Employee(Person):
#     def __init__(self, name, salary):
#         # Inherits name prop from parent class
#         super(Employee, self).__init__(name)
#         # Class Employee has-a salary
#         self.salary = salary
#
#
# # Make a Class Fish that is-a object
# class Fish(object):
#     pass
#
#
# # Make a class Salmon that is a Fish
# class Salmon(Fish):
#     pass
#
#
# # Make a class Halibut that is-a fish
# class Halibut(Fish):
#     pass
#
#
# # Set rover to an instance of class Dog that has-a name Rover
# rover = Dog("Rover")
#
#
# # Set satan to an instance of class Cat that has-a name Satan
# satan = Cat("Satan")
#
#
# # Set mary to an instance of class Person that has a name Mary
# mary = Person("Mary")
#
#
# # From mary get the pet attribute and set it to satan
# mary.pet = satan
#
#
# # Set frank to an instance of class Employee that has-a name of Frank and a salary of 120000
# frank = Employee("Frank", 120000)
#
#
# # From frank get the pet attribute and set it to rover
# # Frank has-a pet named rover
# frank.pet = rover
#
#
# # Set flipper to an instance of class Fish
# # flipper is-a instance of Fish
# flipper = Fish()
#
#
# # Set crouse to an instance of class Salmon
# # crouse is-a instance of Salmon
# crouse = Salmon()
#
#
# # Set harry to an instance of Halibut
# # harry is-a instance of class Halibut
# harry = Halibut()
