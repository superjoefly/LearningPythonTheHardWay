# Exercise 11: Asking Questions

# raw_input() prompts for user input

# print "How old are you?",
# age = raw_input()
# print "How tall are you?",
# height = raw_input()
# print "How much do you weight?",
# weight = raw_input()
#
# print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

# # Practice:
# print "What is your first name?",
# first_name = raw_input();
# print "What is your last name?",
# last_name = raw_input();
# print "How old are you?",
# age = raw_input();
#
# print "So you're first name is %r, your last name is %r and you are %r years old." % (first_name, last_name, age);
#
# # Get number from user:
# print "Give me a number between 1 and 10.",
# user_number = int(raw_input());
# my_number = 10;
#
# difference = my_number - user_number;
#
# print "The difference between my number and the user's number is %r." % difference;



# # Exercise 12: Prompting People
#
# # Store user data in variable and print:
# y = raw_input('Name? ')
# print y;
#
# # Previous example using only prompts:
# first_name = raw_input('What is your name? ')
# last_name = raw_input('What is your last name? ')
# age = raw_input('How old are you? ')
#
# print("So your first name is %r, your last name is %r and you are %r years old!") % (first_name, last_name, age);



# # Exercise 13: Parameters, Unpacking, Variables
#
# # Get user input for more variables
# hair_color = raw_input('Hair Color? ')
# eye_color = raw_input('Eye Color? ')
#
# # Import argv module
# from sys import argv
#
# # Unpack variables passed to script (will pull out variables in the order passed in ... destructuring?)
# script, first_name, middle_name, last_name = argv
#
# # Print out variables
# print "The script is:", script
# print "Your first name is:", first_name
# print "Your middle name is:", middle_name
# print "Your last name is:", last_name
#
# print "Your hair color is:", hair_color
# print "Your eye color is:", eye_color



# # Lesson 14: Prompting and Passing
#
# # Import argv Module
# from sys import argv
#
# # Unpack variables
# script, user_name, avatar = argv
#
# # Define prompt-text
# prompt = 'Huh? '
#
# print "Hi %s, I'm the %s script. Your avatar has been saved as %s" % (user_name, script, avatar)
#
# print "I'd like to ask you a few questions."
#
# print "Do you like me %s?" % user_name
# likes = raw_input(prompt)
#
# print "Where do you live %s?" % user_name
# lives = raw_input(prompt)
#
# print "What kind of computer do you have?"
# computer = raw_input(prompt)
#
# print '''
#     Alright...you said %r about liking me.
#     You live in %r. I wonder where that is...
#     You have a %r computer...nice!
#     By the way...I really like the %s avatar!
# ''' % (likes, lives, computer, avatar)



# # Exercise 15: Reading Files
#
# # Import the argv module from python system package
# from sys import argv
#
# # Unpack variables from argv
# script, filename = argv
#
# # Open the file (returns a file object)
# my_file = open(filename)
#
# # Give user some feedback
# print "Here's the name of the file: %r" % filename
#
# # Read the file
# print "Reading file: %r" % filename
# print my_file.read()
#
# # Prompt for file name again
# print "Type the file name again: "
# file_name_again = raw_input("> ")
#
# # Open the file again (returns a file object)
# my_file_again = open(file_name_again)
#
# # Read the file again
# print "Reading file: %r again!" % filename
# print my_file_again.read()
