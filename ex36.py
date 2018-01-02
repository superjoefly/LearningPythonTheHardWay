# # Exercise 36: Designing and Debugging
#
# # # Rules for If-Statements:
# # every if must have and else
# # use a die function in the else block if it should not be run
# # try not to nest if-statements
# # use blank lines to separate if, elif and else statements
# # boolean tests should be simple...use variables if necessary
#
# # Rules for Loops:
# # Avoid while-loops if possible
# # Use for-loops freely, especially when there is a fixed number of things to loop over
#
# # Tips for Debugging:
# # Don't use debuggers
# # Use 'print' for debugging
# # Debug as you build your program
#
# # My Game
#
# from sys import exit
#
# hit_head = "You hit your head on some rocks above and got knocked out!"
#
# fell_into_hole = "You fell into a hole and got killed!"
#
# starved_to_death = "You sat around hoping to be saved but ended up dying of starvation..."
#
# def die(why):
#     print why
#     exit(0)
#
# def knocked_out(message, next):
#     print message
#     next()
#
# def try_again(next):
#     next()
#
# def trap_door():
#             print "You found a trap door on the floor..."
#             print "Would you like to open the trap door?"
#             print '''
#                 1. Open trap door
#                 2. Keep crawling around on the floor
#                 3. Stand up and walk around
#             '''
#             response2 = raw_input("> ")
#             if response2 == "1":
#                 loud_room()
#
#             elif response2 == "2":
#                 die(fell_into_hole)
#
#             elif response2 == "3":
#                 knocked_out(hit_head, dark_room)
#
# def new_world():
#     print "You open the door and see a blue sky with floating orbs."
#     print "What would you like to do..."
#     print """
#         1. Close the door, it's too scary!
#         2. Lay down and take a nap.
#         3. Walk out the door!
#     """
#
#     response = raw_input("> ")
#     if response == "1":
#         print "We're never gonna get anywhere at this rate."
#         die("The others decided to eat you for food!")
#
#     elif response == "2":
#         dark_room()
#
#     elif response == "3":
#         die("You discovered a New World free from all the BS! You Win!!!")
#     else:
#         die("You suck!")
#
# def trap_door():
#     print """
#     You found a trap door on the floor!
#     There is some very loud music playing!
#     There are some people below yelling at you!
#     You can't understand them because of the music...
#     """
#     print """
#         1. Drop down into the room below.
#         2. Close the trap door and look around the dark room some more.
#         3. Yell back at the people below.
#     """
#     people_hear = False
#     player_careless = True
#
#     while True:
#         response = raw_input("> ")
#
#         if response == "1" and player_careless:
#             print "You jumped down and broke your leg..."
#             print "The others decided they should use you for food."
#             print "You tried to get away but couldn't!"
#             die("Game over!!!")
#
#         if response == "1" and not player_careless:
#             print "You drop down into the room and turn off the loud music!"
#             print "The people need your help getting out..."
#             print """
#             1. Attempt to help the people escape.
#             2. Start crying.
#             3. Ignore them and worry about yourself.
#             """
#
#             response2 = raw_input("> ")
#
#             if response2 == "1":
#                 print "You look around the room for hours and eventually find a hidden door in one of the walls."
#                 new_world()
#
#             elif response2 == "2":
#                 print "Well, crying didn't help anything!"
#                 die("They got tired of you and killed you!")
#
#             elif response2 == "3":
#                 die("They got angry with you and ate you for food!")
#
#             else:
#                 die("I have no idea what that means???")
#
#         elif response == "2":
#             die(fell_into_hole)
#
#         elif response == "3" and not people_hear:
#             print "Well that was useless...they can't hear you either!"
#             people_hear = True
#             player_careless = False
#
#         elif response == "3" and people_hear:
#             print "They're screaming for help!!!"
#             print "You should probably go down and help them!"
#
#         else:
#             die("I have no idea what that means???")
#
# def dark_room():
#     print "You wake up in a dark room and can't see anything!"
#     print "What do you want to do?"
#     print '''
#         1. Sit around and hoping someone comes to save you.
#         2. Stand up and walk around looking for a way out.
#         3. Crawl around the floor looking for a way out.
#     '''
#     response = raw_input("> ")
#
#     if response == "1":
#         print "No one came to save you!"
#         print "Would you like to keep waiting or try again?"
#         print '''
#             1. Keep waiting
#             2. Try again
#         '''
#         response2 = raw_input("> ")
#         if response2 == "1":
#             die(starved_to_death)
#         elif response2 == "2":
#             try_again(dark_room)
#
#     elif response == "2":
#         knocked_out(hit_head, dark_room)
#
#     elif response == "3":
#         trap_door()
#
#     else:
#         die("I have no idea what that means???")
#
# dark_room()
