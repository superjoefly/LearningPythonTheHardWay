# Exercise 44: Inheritance vs Composition

# Inheritance:

# Make a class Foo that inherits from Bar
# class Foo(Bar):

# Foo will inherit the properties and methods of Bar




# # Implicit Inheritance:
# # Make a class Parent that is an object
# # Parent is a base-class
# class Parent(object):
#
#     def implicit(self):
#         print "Implicit method of the Parent Object"
#
# # Make a class Child that inherits from Parent
# # Child is a sub-class of Parent
# class Child(Parent):
#     # Empty block - nothing new to define
#     pass
#
# dad = Parent()
# son = Child()
#
# dad.implicit()
# son.implicit()


# # Override Explicitly
# class Parent(object):
#
#     def implicit(self):
#         print "Implicit method of the Parent class"
#
# class Child(Parent):
#
#     # Overrides the implicit method of the Parent class
#     def implicit(self):
#         print "Implicit method of the Child class"
#
# dad = Parent()
# son = Child()
#
# dad.implicit()
# son.implicit()



# # Override using Super:
# class Parent(object):
#
#     def altered(self):
#         print "Hi, I'm the Parent!!"
#
# class Child(Parent):
#
#     def altered(self):
#         print "Child before Parent altered"
#
#         # Call the altered method of the Parent Class
#         super(Child, self).altered()
#         # Print
#         print "Child after Parent altered"
#
# dad = Parent()
# son = Child()
#
# dad.altered()
# son.altered()



# # All Three Combined:
# class Parent(object):
#
#     def who_am_i(self):
#         print "I'm the parent!"
#
# # make a class Child that inherits from Parent
# class Child(Parent):
#     # pass
#     # Override the who_am_i() method of the parent class
#     def who_am_i(self):
#         print "I'm the child!"
#         # Call the who_am_i() method of the parent class
#         super(Child, self).who_am_i()
#         # Continue to print from the Child
#         print "I'm the child again!"
#
# # Set dad to an instance of Parent
# dad = Parent()
# # Set son to an instance of Child
# son = Child()
#
# dad.who_am_i()
# son.who_am_i()



# # Using super() with __init__
# class Parent(object):
#
#     def i_am(self):
#         print "I'm the parent"
#
# # make a class Child that inherits from Parent
# class Child(Parent):
#
#     # Initializes the Child Class
#     def __init__(self):
#         # Initializes the Parent Class
#         super(Child, self).__init__()
#         print "Whatever"
#
# message = 'Hello there!'
#
# dad = Parent()
# son = Child()
#
# dad.i_am()
# son.i_am()



# # Composition
# class Animal(object):
#
#     def i_am(self):
#         print "I am an animal!"
#
# class Dog(Animal):
#
#     def __init__(self, type):
#         self.type = type
#
#         # Gives us access to the parent within the child
#         self.animal = Animal()
#
#     def i_am(self):
#         print "I am a %s" % self.type
#
#     # Define a new method that calls the parent method
#     def parent_i_am(self):
#         self.animal.i_am()
#
#
# animal = Animal()
# dog = Dog('doggy')
#
# animal.i_am() # I am an animal!
# dog.i_am() # I am a doggy
# dog.parent_i_am() # I am an animal!


# When to use Inheritance vs Composition

# Three rules:

# 1. Avoid multiple inheritance (inheriting from more than one class)
# 2. Use composition to package up code into modules that can be used in different programs
# 3. Only use inheritance when there are clearly related reusable pieces of code that fit under a single common concept
