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



# Exercise 17: Copy One File to Another

from sys import argv
from os.path import exists

# Unpack variables from argv
script, from_file, to_file = argv

print "Copying files from %s to %s" % (from_file, to_file)

# Method Chaining (open and read)
data = open(from_file).read() # closes automatically

print "The input file is %d bytes long..." % len(data)
print "The output file exists: %r" % exists(to_file)

raw_input("Ready to copy...hit 'enter' to continue or 'ctrl+c' to abort...")

out_file = open(to_file, 'w')
out_file.write(data)

print "Done!"

out_file.close()

# All in One
# open(to_file, 'w').write(open(from_file).read())



# Exercise 18: Names, Variables, Code, Functions
