# # Exercise 16: Reading and Writing Files
#
# # Import argv module from sys package
# from sys import argv
#
# # Unpack variables (passed in terminal) from argv variable
# script, filename = argv
#
# print "We're going to erase %r" % filename
#
# print "If you don't want that, hit 'ctrl+c'"
#
# print "If you do want that, hit 'return'"
#
# # Waiting for user input...
# raw_input("?")
#
# # If user chooses 'enter'
# print "Opening file..."
#
# # Open file for writing - result is stored in variable (target)
# target = open(filename, 'w')
#
# print "Truncating the file...goodbye!"
#
# # Truncates (empties) the file
# target.truncate()
#
# print "Now I'm going to ask you for three lines..."
#
# # Define some variables using user's raw input
# line1 = raw_input("Line 1: ")
# line2 = raw_input("Line 2: ")
# line3 = raw_input("Line 3: ")
#
# print "I'm going to write these to the file..."
#
# # Writes to file
# target.write(line1)
# target.write("\n")
#
# target.write(line2)
# target.write("\n")
#
# target.write(line3)
# target.write("\n")
#
# print "And finally we close the file..."
#
# # Closes the file
# target.close()



# #PRACTICE (Open Read Write)
#
# # Import argv module
# from sys import argv
#
# # Unpack data from argv and store in variable
# script, filename = argv
#
# # Options: open(filename, r = read, w = write, a = append)
# # Modifiers: open(filename, r+, w+, a+) open in more than one mode
#
# # Open File for READ and store in variable
# print "Opening file %r for reading..." % filename
# target = open(filename) # read is default mode
#
# # READ and PRINT contents
# print "Reading file..."
# print target.read()
#
# # Close the file
# print "Closing file..."
# target.close()
#
# # Continue Script?...
#
# # Request user input
# raw_input("Write to file? Hit ctrl+c to cancel or 'return' to continue...")
#
# # Open file for Read and Write (automatically truncates the file)
# print "Opening file for reading and writing..."
# target = open(filename, 'r+')
#
#
# # Define variables to write to file
# line1 = "Hello there!"
# line2 = "What's been going on?"
# line3 = "I hope you're having a great night!"
#
# # Write to file
# print "Writing to file..."
# target.write(line1 + "\n" + line2 + "\n" + line3)
#
#
# target.flush() # Flushes internal buffer
# target.seek(0) # Seek to first position in file so we can Read
#
#
# # Request user input
# raw_input("Read file again? Hit ctrl+c to cancel or 'return' to continue...")
#
#
# # Read and Print File
# print "Reading file..."
# print target.read()
#
# # Close file
# print "Closing file :-)"
# target.close()



# # Exercise 17: Copy One File to Another
#
# from sys import argv
# from os.path import exists
#
# # Unpack variables from argv
# script, from_file, to_file = argv
#
# print "Copying files from %s to %s" % (from_file, to_file)
#
# # Method Chaining (open and read)
# data = open(from_file).read() # closes automatically
#
# print "The input file is %d bytes long..." % len(data)
# print "The output file exists: %r" % exists(to_file)
#
# raw_input("Ready to copy...hit 'enter' to continue or 'ctrl+c' to abort...")
#
# out_file = open(to_file, 'w')
# out_file.write(data)
#
# print "Done!"
#
# out_file.close()
#
# # All in One
# # open(to_file, 'w').write(open(from_file).read())



# # Exercise 18: Names, Variables, Code, Functions
#
# # Similar to scripts with argv
# def print_two(*args):
#     arg1, arg2 = args
#     print "arg1: %r, arg2: %r" % (arg1, arg2)
#
# # Two arguments
# def print_two_again(arg1, arg2):
#     print "arg1: %r, arg2: %r" % (arg1, arg2)
#
# # One argument
# def print_one(arg1):
#     print "arg1: %r" % arg1
#
# # No arguments
# def print_none():
#     print "I got nothin..."
#
# # Call functions passing in strings as arguments
# print_two("Joey", "Atwood")
# print_two_again("Joey", "Atwood")
# print_one("David")
# print_none()
#
# # Practice
#
# def checklist(*items):
#     item1, item2, item3 = items
#     print "\nitem1: %r, \nitem2: %r, \nitem3: %r" % (item1, item2, item3)
#
# checklist('Go to work', 'Go to the store', 'Walk the dog')



# # Exercise 19: Functions and Variables
#
# def checklist(*items):
#     item1, item2, item3 = items
#     print ("\nitem1: %r, \nitem2: %r, \nitem3: %r") % (item1, item2, item3)
#
# # Pass strings as arguments
# checklist('Go to store', 'Walk dog', 'Go to work')
#
# my_item1 = 'Study hard'
# my_item2 = 'Be persistent'
# my_item3 = 'Dont give up'
#
# # Pass variables as arguments:
# checklist(my_item1, my_item2, my_item3)
#
# # Pass operations as arguments:
# checklist("Watch " + "movie", "Read " + "book", 5 + 5)
#
# #############
#
# # Define variables directly inside function:
# def newlist(item1 = 'red', item2 = 'blue', item3 = 'green'):
#     print("\nitem1: %r, \nitem2: %r. \nitem3: %r") % (item1, item2, item3)
# # Call the function
# newlist()



# # Exercise 20: Functions and Files
#
# # Import argv module
# from sys import argv
#
# # Unpack variables from argv
# script, input_file = argv
#
# # Open file and store in variable
# current_file = open(input_file)
#
#
#
# print "First we'll printing the whole file...\n"
#
# # Request user input to continue
# raw_input("Ready? Hit enter to continue or ctrl+c to quit...")
#
# # Define function to read and print file
# def print_all(f):
#     # read and print opened file
#     print f.read()
#
# print_all(current_file)
#
#
# #############
#
#
# print "Now lets rewind to the first position in the file..."
#
# # Define function to seek back to position 0
# def rewind(f):
#     f.seek(0)
#
# rewind(current_file)
#
#
# #############
#
#
# print "Now, lets print three lines:"
#
# raw_input("Ready? Hit enter to continue or ctrl+c to quit...")
#
# # Define function to print lines
# def print_line(line_count, f):
#     print line_count, f.readline()
#
# current_line = 1 # Current line is 1
# print_line(current_line, current_file)
#
# current_line += 1 # Increments current_line to 2
# print_line(current_line, current_file)
#
# current_line += 1 # Increments current_line to 3
# print_line(current_line, current_file)
#
#
# ###########
#
#
# # Close the currently opened file
# current_file.close()
