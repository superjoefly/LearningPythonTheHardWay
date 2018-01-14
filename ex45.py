# # Make a Game
#
# from sys import exit
# from random import randint
#
# class Room(object):
#
#     def enter(self):
#         print 'Not configured...'
#         exit(1)
#
# class Engine(object):
#
#     def __init__(self, room_map):
#         self.room_map = room_map
#
#     def play(self):
#         current_room = self.room_map.opening_room()
#         last_room = self.room_map.next_room('finished')
#
#         while current_room != last_room:
#             print '-------------'
#             next_room_name = current_room.enter()
#             current_room = self.room_map.next_room(next_room_name)
#
#         current_room.enter()
#
# class GoldRoom(Room):
#
#     def enter(self):
#         print "You have entered the Gold Room!"
#         print "You don't see anyone around."
#         print "You notice three doors on the floor numbered from 1 to 3"
#         print "Which one do you choose?"
#
#         good_choice = randint(1, 3)
#         guess = raw_input("> ")
#
#         if int(guess) != good_choice:
#             print "You chose door %s" % guess
#             print "This wasn't a very good choice!"
#             return 'death'
#
#         else:
#             print "You chose door %s" % guess
#             print "Lucky You!"
#             return 'finished'
#
#
# class SilverRoom(Room):
#
#     def enter(self):
#         print "You have entered the Silver Room!"
#         print "You look around and see a green, one-eyed monster!"
#         print "The monster thinks you would make a good treat, and starts"
#         print "to chase you around the room!"
#         print "You can either run back into the bronze room and try the other door,"
#         print "or try one of your weapons..."
#         print "What do you want to do?"
#         print "1. return to Bronze Room to try another door!"
#         print "2. try using a weapon!"
#
#         choice = raw_input('> ')
#
#         if choice == '1':
#             return 'bronze_room'
#
#         elif choice == '2':
#
#             print "You have 3 weapons...which one would you like to try?"
#             print "1. sword"
#             print "2. knife"
#             print "3. potion"
#
#             weapon = raw_input('> ')
#
#             if weapon == '1':
#                 print "You chose the %s, but it didn't help at all...the monster caught you and ate your head!" % weapon
#                 return 'death'
#
#             elif weapon == '2':
#                 print "You attacked that huge monster with a little knife??"
#                 print "What's wrong with you?"
#                 print "The monster was very satisfied with his meal..."
#                 return 'death'
#
#             elif weapon == '3':
#                 print "You took a position and through it into the monsters face!"
#                 print "The monster shrunk down to a cute little fuzzy thing!"
#                 print "Now he's rubbing up agains your leg...looks like you made a friend!"
#                 return 'gold_room'
#
#             else:
#                 print "You stumled around looking for your %s but couldn't find it!" % weapon
#                 return 'death'
#
#         else:
#             print "I have no idea what that means..."
#             return 'bronze_room'
#
#
# class BronzeRoom(Room):
#
#     def enter(self):
#         print "You have entered the Bronze Room!"
#         print "You don't see anyone around."
#         print "You're not sure what to do, by know you must do something..."
#         print "There is a door to your right, and a door to your left."
#         print "Which door do you choose?"
#         door = raw_input('> ')
#         if door == 'left':
#             return 'silver_room'
#         else:
#             return 'gold_room'
#
#
# class Finished(Room):
#
#     def enter(self):
#         print "You won the game!!!"
#         return 'finished'
#         exit(1)
#
# class Death(Room):
#
#     message = [
#         "You lost!! Dude?? You Suck!",
#         "I think you may wanna stick with Tetris!",
#         "Oh, well...at least you tried!",
#         "I knew you couldn't do it!!!"
#     ]
#
#     def enter(self):
#         print Death.message[randint(0, len(self.message) - 1)]
#         exit(1)
#
#
# class Map(object):
#
#     rooms = {
#         'gold_room': GoldRoom(),
#         'silver_room': SilverRoom(),
#         'bronze_room': BronzeRoom(),
#         'death': Death(),
#         'finished': Finished()
#     }
#
#     # Use an init function to define the first room
#     def __init__(self, first_room):
#         self.first_room = first_room # bronze_room
#
#     def next_room(self, room_name):
#         return Map.rooms.get(room_name)
#
#     def opening_room(self):
#         return self.next_room(self.first_room)
#
#
# map = Map('bronze_room')
# game = Engine(map)
# game.play()
