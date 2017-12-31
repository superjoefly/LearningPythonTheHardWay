# Exercise 27: Memorizing Logic (booleans)

# # Exercise 28: Boolean Practice
#
# True and True -> true
#
# False and False -> false
#
# 1 == 1 and 2 == 1 -> false
#
# "test" == "test" -> true
#
# 1 == 1 or 2 == 1 -> true
#
# True and 1 == 1 -> true
#
# False and 0 != 0 -> false
#
# True or 1 == 1 -> true
#
# "test" == "testing" -> false
#
# 1 != 0 and 2 == 1 -> false
#
# "test" != "testing" -> true
#
# "test" == 1 -> false
#
# not (True and False) -> false
#
# not (1 == 1 and 0 != 1) -> false
#
# not (10 == 1 or 1000 == 1000) -> true
#
# not (1 != 10 or 3 == 4) -> true
#
# not ("testing" == "testing" and "Zed" == "Cool Guy") -> false
#
#
#
# true                false          false
# 1 == 1 and not ("testing" == 1 or 1 == 0) -> true
#
#
#
#                                    true
#                               true  or  false
#         false                 false     true
# "chunky" == "bacon" and not (3 == 4 or 3 == 3) -> false
#
#
# true         and                      true
#                          false                    true
# true                     true                     false
# 3 == 3 and not ("testing" == "testing" or "Python" == "Fun") -> true


# >>> True and True
# True
# >>> False and False
# False
# >>> True and False
# False
# >>> True or False
# True
# >>> 1 == 1 and 2 == 1
# False
# >>> "test" == "test"
# True
# >>> 1 == 1 or 2 != 1
# True
# >>> True and 1 == 1
# True
# >>> False and 0 != 0
# False
# >>> True or 1 == 1
# True
# >>> "test" == "testing"
# False
# >>> "test" != "testing"
# True
# >>> True or 1 == 1
# True
# >>> 1 != 0 and 2 == 1
# False
# >>> "test" == 1
# False
# >>> "test" == 1
# False
# >>> not (True and False)
# True
# >>> not (1 == 1 and 0 != 1)
# False
# >>> not (10 == 1 or 1000 == 1000)
# False
# >>> not (1 != 10 or 3 == 4)
# False
# >>> not ("testing" == "testing" and "Zed" == "Cool")
# True
# >>> 1 == 1 and not ("testing" == 1 or 1 == 0)
# True
# >>> "chunky" == "bacon" and not (3 == 4 or 3 == 3)
# False
# >>> 3 == 3 and not ("testing" == "testing" or "Python" == "Fun")
# False


# >>> True and 1
# 1
# >>> True or 1
# True
# >>> False and 1
# False
# >>> 1 and False
# False
# >>> 1 and True
# True
# >>> True and 1



# # Exercise 29: If Statement: will only execute if statement evaluates to true
#
# people = 20
# cats = 30
# dogs = 15
#
# # Less Than / Greater Than
# if people < cats: # true
#     print "More cats than people..."
#
# if people > cats: # false
#     print "More people than cats..."
#
# if people < dogs: # false
#     print "More dogs than people..."
#
# if people > dogs: # true
#     print "More people than dogs..."
#
# # Add 5 to dogs
# dogs += 5
#
# # Greater Than or Equal To / Less Than or Equal to
# if people >= dogs: # true
#     print "People are greater than or equal to dogs..."
#
# if people <= dogs: # true
#     print "People are less than or equal to dogs..."
#
# # Equal to
# if people == dogs: # true
#     print "People are equal to dogs"



# # Exercise 30: Else If (elif) Statement
#
# people = 50
# cars = 30
# buses = 20
#
# if cars > people: # false
#     print "More cars than people"
# elif cars < people: # true
#     print "More people than cars"
# else: # default
#     print "Oh whatever!"
#
# if buses > cars: # false
#     print "That's too many buses!"
# elif cars > buses: # true
#     print "Okay, that's cool!"
# else: # default
#     print "This is default!"
#
#
# if people > buses: # true
#     print "We should take the bus!"
# else: # default
#     print "Let's just stay home :-("
#
# if cars > people or buses < cars:
#     print "Okay, we're taking the bus!"
#
# if cars < people and buses < cars:
#     print "I guess we could take either one..."

# Note: only the first statement that evaluates to true will run
