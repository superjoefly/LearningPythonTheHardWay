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
