# Exercise 38: Lists - Arrays

# my_list = ['Hello']
#
# my_list.append('World')
#
# print my_list
#
# # Class Example
#
# class Thing(object):
#     def test(hi):
#         print "Hi"
#
# a = Thing()
# a.test()

# # Practice
#
# my_list = ['pray', 'meditate', 'study', 'work', 'workout', 'sleep']
# list_length = len(my_list)
# print "My list currently has %d items." % list_length
#
# new_items = ['read', 'movie', 'walk', 'shop']
#
# # while the length of my_list is not equal to 10
# while len(my_list) != 10:
#     # pop off last item in new_items and store in variable
#     next_item = new_items.pop()
#     # print statement with variable (next_item)
#     print "Adding %s" % next_item
#     # append the new item to end of my_list
#     my_list.append(next_item)
#     # print statement with variable (length of my_list)
#     print "There are now %d items in my list." % len(my_list)
#
# # print my_list
# print my_list
#
# print "The second item is: %s" % my_list[1]
# print "The last item is: %s"% my_list[-1]
# print "Using 'pop' will pop off the last item: %s" % my_list.pop()
# # using a space, join my_list
# print ' '.join(my_list)
# # using a hashtag, join the 4th and 5th elements of my_list
# print '#'.join(my_list[3:5])
#
# # Explanation
# # ' '.join(things) is the same as join(' ', things)
# # however...join(' ', things) won't work




# Exercise 39: Dictionaries

# my_list = ['study', 'work', 'play', 'second']
# print my_list[1] # study
#
# # Redifine item in my_list
# my_list[1] = 'first'
# print my_list[1] # first
#
# print my_list
#
# # We can only use numbers to pull items from a list
#
# ## A Dict allows us to associate one thing to another no matter what it is.
#
# # Define an object
# profile = {'name': 'Joey', 'age': 37, 'height': '5\'11', 'city': 'Boulder'}
# print profile
# print profile['name'] # Joey
# print profile['age'] # 37
# print profile['height'] # 5'11
# print profile['city'] # Boulder
#
# # Change value of element in profile
# profile['age'] = 38
# print profile['age'] # 38
#
# # Add to profile object
# profile[1] = 'New'
# profile[2] = 'Something'
# print profile
#
# # Delete from profile object
# del profile[1]
# del profile[2]
# print profile


# # Practice
# # Define some states
# states = {
#     'Oregon': 'OR',
#     'Florida': 'FL',
#     'California': 'CA',
#     'New York': 'NY',
#     'Michigan': 'MI'
# }
#
# # Define some cities
# cities = {
#     'CA': 'San Francisco',
#     'MI': 'Detroit',
#     'FL': 'Jacksonville'
# }
#
# # Add some cities to cities list
# cities['NY'] = 'New York'
# cities['OR'] = 'Portland'
#
# # Print out some cities
# print '-' * 10
#
# print 'NY State has: ', cities['NY']
# print 'OR State has: ', cities['OR']
#
# # Print some states
# print '-' * 10
#
# print "Michigan's abbreviation is ", states['Michigan']
# print "Florida's abbreviation is ", states['Florida']
#
# # using state then city's dict
# print '-' * 10
#
# print "Michigan has: ", cities[states['Michigan']]
# print "Florida has: ", cities[states['Florida']]
#
# # Print every state abbreviation
# print '-' * 10
#
#     #key   #value
# for state, abbrev in states.items():
#     print "%s is abbreviated %s" % (state, abbrev)
#
# # Pring every city in state
# print '-' * 10
#
#     #key    #value
# for abbrev, city in cities.items():
#     print "%s has the city %s" % (abbrev, city)
#
# # Do both at the same time
# print '-' * 10
#
# for state, abbrev in states.items():
#     print "%s state is abbreviated %s and has a city %s" % (state, abbrev, cities[abbrev])
#
# # Safely get an abbreviation by state that might not be there
# print '-' * 10
#
# state = states.get('Texas', None)
# if not state:
#     print "Sorry, no Texas..."
#
# # Get a city with a default value
# print '-' * 10
#
# city = cities.get('TX', 'Does not exist')
# print "The city for the state 'TX' is: %s" % city



# Exercise 40: Modules, Classes and Objects

# # DICT - [key]
# friend = {'first_name': 'Joey', 'last_name': 'Atwood', 'age': 38}
# print friend['first_name']


# # MODULES - .key
# # Import the module
# import my_module
# # Call the person method of my_module
# my_module.full_name() # My name is Joey!
# # Print the address variable of my_moudle
# print my_module.first_name



# # CLASSES - use the '.' operator - build objects

# # Practice 1
#
# class Person(object):
#     def __init__(self, arg1, arg2, arg3):
#         self.first_name = arg1
#         self.last_name = arg2
#         self.age = arg3
#
#     def get_full_name(self):
#         print "%s %s is %d years old" % (self.first_name, self.last_name, self.age)
#
# # Instantiate a new Person object
# friend1 = Person('Joey', 'Atwood', 38)
# print friend1.first_name
# print friend1.last_name
# print friend1.age
# print friend1.get_full_name()
#
# print '-' * 10
#
# friend2 = Person('John', 'Doe', 49)
# print friend2.first_name
# print friend2.last_name
# print friend2.age
# print friend2.get_full_name()


# # Practice 2
#
# class Song(object):
#     def __init__(self, lyrics, name):
#         self.lyrics = lyrics
#         self.name = name
#
#     def sing_song(self):
#         print self.lyrics % self.name
#
# name = 'Joey'
# name = 'John'
#
# hb_lyrics = '''
#     Happy birthday to you...
#     Happy birthday to you...
#     Happy birthday dear %s...
#     Happy birthday to you!!!
# '''
#
# # Instantiate new Song object and pass in variable hp_lyrics
# happy_birthday = Song(hb_lyrics, name)
#
# happy_birthday.sing_song()


# # Practice 3
#
# class Employees:
#     'Common base class for all employees'
#     empCount = 0
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employees.empCount += 1
#
#     def displayCount(self):
#         print "Total employees: ", Employees.empCount
#
#     def displayEmployee(self):
#         print "Name: ", self.name, ", Salary: ", self.salary
#
# emp1 = Employees('John', 2000)
# emp2 = Employees('Jane', 3000)
#
# emp1.displayEmployee()
# emp2.displayEmployee()
#
# print "The total number of employees is: ", Employees.empCount
