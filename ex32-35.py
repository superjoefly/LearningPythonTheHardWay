# # Exercise 32: For-In Loop
#
# # Note: the python name for an array is a 'list'
#
# colors = ['red', 'green', 'blue']
# for color in colors:
#     print color
#
# for color in colors:
#     print "The color is %s" % color
#
# # Mixed List
# items = ['one', 1, 'two', 2, 'three', 3]
# for item in items:
#     print "The item is %r" % item
#
# #############
#
# # Building an Array
# numbers = []
#
# # Uses range() function: first number inclusive,
# # second number exclusive
# for i in range(1, 6):
#     print "Adding %d to the list." % i
#     # adds each item to end of array
#     numbers.append(i)
#     # To reverse order, use insert()
#     # numbers.insert(0, i)
#     numbers.reverse()
#
# for i in numbers:
#     print i
#
#
# # Reverse List
# directions = ['Up', 'Down', 'Left', 'Right']
# for i in reversed(directions):
#     print i



# Exercise 33: While Loops

# i = 0
# numbers = []
#
# while i < 6:
#     numbers.append(i) # appends value of i to end of list
#     print i # prints value of i for each iteration
#     i += 1  # increments i
#
# print numbers # prints numbers list once while loop is completed
#
# for num in numbers: # loops through numbers list
#     print num       # prints each number in list

# # As Function:
# def number_loop(count, limit, increment):
#     while count < limit: # evaluates to true or false
#         print count      # prints value of count
#         count += increment       # increments count by 1
#
# number_loop(1, 10, 2)

# # Using For Loop
# def number_loop():
#     for num in range(1, 6):
#         print num
#
# number_loop()




# # Exercise 34: Accessing Elements of List
#
# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
#
# favorite_color = colors[0]
# print favorite_color
#
# last_color = colors[5]
# print last_color
#
# # Grab multiple elements from list:
# from operator import itemgetter # Import 'itemgetter' module
# other_colors = [1, 2, 3, 4] # Define index to get
# print itemgetter(*other_colors)(colors) # Print using itemgetter



# # Exercise 35: Branches and Functions
#
# from sys import exit
#
# def dead(why):
#     print why
#     exit(0)
#
# def gold_room():
#     print "You open a door and the room is full of gold! How much do you take?"
#
#     next = raw_input("> ")
#     if next.isdigit(): # checks to see if number was typed
#         how_much = int(next)
#     else:
#         dead("Only numbers allowed!")
#
#     if how_much < 50:
#         print "Not the greedy type, eh? You WIN!!!"
#         exit(0)
#     else:
#         dead("You greedy bastard!")
#
# # gold_room()
#
# def bear_room():
#     print "You open a door and there is a bear in the room!"
#     print "The bear has a bunch of honey..."
#     print "The bear is blocking the next door!"
#     print "How are you going to get to the next door??"
#     bear_moved = False
#
#     while True:
#         print ("1. take the honey\n2. taunt the bear\n3. open door")
#
#         next = raw_input("> ")
#
#         if next == "1":
#             dead("Nice try...you're gone buddy!")
#         elif next == "2" and not bear_moved:
#             print "The bear moved away from the door!"
#             bear_moved = True
#         elif next == "2" and bear_moved:
#             print "The bear got angry and attacked you!"
#         elif next == "3" and not bear_moved:
#             print "The bear didn't move!!!"
#         elif next == "3" and bear_moved:
#             gold_room()
#         else:
#             print "Waiting..."
#
# # bear_room()
#
# def cathula_room():
#     print "Here you see the great evil Cathula!"
#     print "It stares at you and you start to go insane."
#     print "Do you flee for your life or eat your head??"
#
#     print "1. flee for your life\n2. eat your head"
#
#     next = raw_input("> ")
#
#     if "flee" in next:
#         start()
#     elif "head" in next:
#         dead("Well, that was tasty!")
#     else:
#         cathula_room()
#
#
# def start():
#     print "You are in a dark room!"
#     print "There is a door to your right and left..."
#     print "Which one do you take?"
#
#     next = raw_input("> ")
#
#     if next == "right":
#         bear_room()
#     elif next == "left":
#         cathula_room()
#     else:
#         dead("You stumble around the room until you die of starvation!")
#
# start()
