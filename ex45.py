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
#             next_room_name = current_room.enter()
#             current_room = self.room_map.next_room(next_room_name)
#
#
# class GoldRoom(Room):
#
#     def enter(self):
#         print "You have entered the Gold Room!"
#         print "You don't see anyone around."
#         print "You notice three doors on the floor numbered from 1 to 3"
#         print "Which one do you choose?"
#
#         good_choice = randint(1, 5)
#         guess = raw_input("> ")
#
#         if int(guess) != good_choice:
#             print "You chose door %s" % guess
#             print "This wasn't a very good choice!"
#             return 'death'
#
#         elif int(guess) == good_choice:
#             print "You chose door %s" % guess
#             print "Lucky You!"
#             return 'finished!'
#
#         else:
#             print "I don't know what that means..."
#             return 'bronze_room'
#
#
# class SilverRoom(Room):
#
#     def enter(self):
#         print "You have entered the Silver Room!"
#         print "You don't see anyone around."
#         print "You're not sure what to do, by know you must do something..."
#         print "There is a door to your right, and a door to your left."
#         print "Which door do you choose?"
#         door = raw_input('> ')
#
#         if door == 'left':
#             return 'bronze_room'
#         else:
#             return 'gold_room'
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
#         exit(1)
#
# class Death(Room):
#
#     def enter(self):
#         print "You lost!"
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
