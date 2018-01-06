# Symbol Review

# KEYWORDS

# # and - comparison operator
# print True and True


# # del - delete variable
# my_name = 'Joey'
# print my_name
# del my_name
# print my_name # not defined


# # from - import module
# from sys import argv
# print argv


# # not - comparison operator
# name = raw_input('What is your name?')
# secret = False
# if name == 'Joey' and not secret:
#     print name


# # while - loop while expression evaluates to True
# i = 1
# while i <= 5:
#     print i
#     i += 1


# # as - aliasing
# import math as myAlias
# print myAlias.cos(myAlias.pi) # -1.0


# # elif - else if
# name = 'Joey'
# if name == 'Bruce':
#     print name
# elif name == 'John':
#     print name
# else:
#     print 'Your name is Joey!'


# # global - used to modify global variable inside function
# name = 'Joey'
# def get_name():
#     global name # declare global variable
#     name = 'John'
#     print name
# get_name()
#
# print name # John


# or - comparison operator
# print True or False # True


# # with - ensures __exit__ method is called at end of block
# with open('example.txt', 'w') as my_file:
#     my_file.write('Hello World!')


# assert - used for debugging/testing - check if assumptions are true
# a = 4
# assert a < 4, "The value of a is too small"


# # else - else statement
# a = 5
# if a > 5:
#     print 'Greater than'
# elif a < 5:
#     print 'Less than'
# else:
#     print 'Equal to...'


# if -  if statement (see above)

# # pass - placeholder
# def my_function():
#     pass # avoid indentation error


# # yield - returns a generator
# def generator():
#     for i in range(6):
#         yield i*i
#
# g = generator()
# for i in g:
#     print(i) # print yielded value for each loop in g


# # break - ends the loop
# for i in range(1, 11):
#     if i == 5:
#         break
#     print(i)


# # except, raise, try - used with exceptions (errors)
# def reciprocal(num):
#     try:
#         r = 1/num
#     except:
#         print('Exception Caught')
#         return
#     return r
#
# print(reciprocal(10))
# print(reciprocal(0))

# # # import - import modules
# # # from ... import - import specific attributes or function
# print(math.cos(10))
# import math
# from math import cos
# print(cos(10))


# print - print to console


# # class - used to define a new user-defined class (OOP)
# # - a collection of related attributes and methods
# class Car(object):
#     def get_model(self):
#         print 'Honda'
#     def get_year(self):
#         print '1999'
#
# my_car = Car()
# my_car.get_model() # Honda
# my_car.get_year() # 1999


# # exec - compiles and immediately evaluates a statement or set of statement contained in a string
#
# exec('print(5)') # 5
# exec 'print 5' # 5
# exec('print(5)\nprint(6)') # 5, 6
# exec('if True: print(10)') # 10
# exec('5') # does nothing and returns nothing


# # in - used to test if a sequence contains a value
# a = [1, 2, 3, 4, 5]
# print(5 in a) # True
# print(10 in a) # False


# # raise - raise an exception explicitly
# def reciprocal(num):
#     try:
#         r = 1/num
#     except:
#         if num == 0:
#             raise ZeroDivisionError('Cannot Divide by 0')
#         # print('Exception Caught!')
#             return
#     return r
#
# # print(reciprocal(10))
# print(reciprocal(0))


# # continue - breaks the current iteration of the loop but not the whole loop - 5 is not printed
# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(i)



# finally - used with try...except to close up resources or file streams (is always run)


# # is - used to test if the two variables refer to the same object
# print True is True
# print False is False
# print None is None
# print 4 is 4
# print 'test' is 'test'


# # return - exit function and return value
# def my_function(b):
#     a = b
#     return a
#
# print my_function(10) # 10



# def - used to define a function (see above)



# # for - for loop
# colors = ['red', 'orange', 'yellow']
# for i in colors:
#     print "The color is " + i


# # lambda - used to create an anonymous function (no name)
# a = lambda x: x*2
# for i in range(1, 6):
#     print(a(i)) # pass in i to lambda a as x



# try - try, except, finally
# def my_function():
#     try:
#         print 'Hello World!'/2
#     except:
#         print 'There was an error!'
#     finally:
#         print 'You Rock!!!'
#
# my_function()


##############


# # DATA TYPES
#
# True
#
# False
#
# None
#
# strings
#
# numbers
#
# floats
#
# lists



# Escape Sequences

# \\
#
# \'
#
# \"
#
# \a
#
# \b
#
# \f
#
# \n
#
# \r
#
# \t
#
# \v



# String Formats


# %d
#
# %i
#
# %o
#
# %u
#
# %x
#
# %X
#
# %e
#
# %E
#
# %f
#
# %F
#
# %g
#
# %G
#
# %c
#
# %r
#
# %s
#
# %%




# OPERATORS


# +
#
# -
#
# *
#
# **
#
# /
#
# //
#
# %
#
# <
#
# >
#
# <=
#
# >=
#
# ==
#
# !=
#
# <>
#
# ( )
#
# [ ]
#
# { }
#
# @
#
# ,
#
# :
#
# .
#
# =
#
# ;
#
# +=
#
# - =
#
# *=
#
# /=
#
# //=
#
# %=
#
# **=
