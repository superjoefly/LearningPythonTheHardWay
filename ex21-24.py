# # Exercise 21: Functions Can Return Values
#
# def add(a, b):
#     print "Adding %d to %d" % (a, b)
#     return a + b
#
# def subtract(a, b):
#     print "Subtracting %d to %d" % (a, b)
#     return a - b
#
# def multiply(a, b):
#     print "Multiplying %d to %d" % (a, b)
#     return a * b
#
# def divide(a, b):
#     print "Dividing %d to %d" % (a, b)
#     return a / b
#
# # variable = function (that returns a value)
#
# my_age = add(30, 8)
#
# current_year = subtract(2020, 3)
#
# height = multiply(3, 2)
#
# weight = divide(300, 2)
#
# # Multiline Formatting with Variables
# my_string = '''
#     My age: {0}
#     Current Year: {1}
#     Height: {2}ft
#     Weight: {3}"
#     '''
# # .format modifier
# print my_string.format(my_age, current_year, height, weight)
#
# ###########
#
# formula_result = add(my_age, subtract(height, multiply(weight,
# divide(current_year, 2))))
#
# print "Formula Result: %d" % formula_result
#
# ###########
#
# # Raw Input with Function
# name = raw_input("What is you name? ")
#
# def get_name(username):
#     print "You entered %s!" % username
#
# get_name(name)


# # Exercise 24: Practice
#
# print "Let's practice some stuff..."
#
# # Escape Characters
# print 'It\'s important to know \'bout escapes with \\ backslashes that do \n new-lines and \t tabs'
#
# raw_input("Ready? hit 'enter' to continue!")
#
# poem = '''
#     The world is lovely
#     logic is useless
#     love only counts
#     feelings not words
#     that explain the universe
#     and where it is going
# '''
#
# print "-----------"
# print poem
# print "-----------"
#
# # Math
# raw_input("Now we'll do some math!...ready? Hit 'enter'!")
# result = 10 - 2 + 3 - 6
# print "The result of the above computation should evaluate to %d" % result
#
# def my_function(start):
#     jelly_beans = start * 500 # 5000000
#     jars = jelly_beans / 1000 # 5000
#     crates = jars / 100 # 50
#     return jelly_beans, jars, crates
#
# start = 10000
# beans, jars, crates = my_function(start)
#
# print "With a starting value of %d" % start
# print "We have %d beans, %d jars and %d crates..." % (beans, jars, crates)
#
# # Another way...
#
# print "We can also do it this way..."
#
# # Uses the return values from the function to define the embedded variables:
# print "We'd have %d beans, %d jars and %d crates." % my_function(start)
