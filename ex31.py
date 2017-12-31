# # Exercise 31: Making Decisions
#
# def end_game():
#     print "Game Over : ("
#     play_again()
#
# def play_again():
#     print "Would you like to play again?"
#     try_again = raw_input("Y/N ")
#     if (try_again == "Y") or (try_again == "y"):
#         start_game()
#     elif (try_again == "N") or (try_again == "n"):
#         print "Thanks for playing!"
#     else:
#         print "The ceiling crumbled and fell on your head! Game Over!"
#
# def make_wish():
#     print "What is your wish?"
#     wish = raw_input("> ")
#     if len(wish) > 10:
#         print "Your wish has been granted and you won the game!"
#         play_again()
#     else:
#         print "You've been fooled! Now you spend the rest of your life in an eternal hypnotic state!"
#         end_game()
#
# def start_level_two():
#     print "You beat level one! Good job...move on to Level 2?"
#     start_two = raw_input("Y/N ")
#     if (start_two == "Y") or (start_two == "y"):
#         print "You have started Level 2"
#     else:
#         play_again()
#
# def open_door_one():
#     print "There's a monster here eating a cat...what do you do?"
#     print "1. Try to save the cat!"
#     print "2. Quickly close the door!"
#
#     response_to_monster = raw_input("> ")
#
#     if response_to_monster == "1":
#         print "The monster attacked you! AAAhhhhh!"
#         end_game()
#     elif response_to_monster == "2":
#         print "Smart thinking...you got away! Congratulations!"
#         play_again()
#     else:
#         print "I wouldn't do that if I were you :-O"
#
#         try_door_one_again = raw_input("Would you like to try door one again?  Y/N ")
#
#         if (try_door_one_again == "Y") or (try_door_one_again == "y"):
#             open_door_one()
#         else:
#             end_game()
#
# def open_door_two():
#     print "You are met with a HUGE glaring eye with a spiraling retina promising to grant you a wish..."
#     print "1. Make a wish"
#     print "2. Run - could result in death!"
#     print "3. What was I thinking about again???"
#
#     response_to_eye = raw_input("> ")
#
#     if response_to_eye == "1":
#         make_wish()
#     elif response_to_eye == "2":
#         print "You ran and got away from that evil eye! Good job!"
#         start_level_two()
#     elif response_to_eye == "3":
#         print "You've already been hypnotized!"
#         end_game()
#     else:
#         print "You tricked the eye and won the game! Congrats!"
#
#
# def start_game():
#     print "You enter a dark room with two doors...do you go through Door #1 or Door # 2?"
#
#     door = raw_input("> ")
#
#     if door == "1":
#         open_door_one()
#
#     elif door == "2":
#         open_door_two()
#
#     else:
#         print "You slipped and hit your head on a rock!"
#         end_game()
#
# start_game()
