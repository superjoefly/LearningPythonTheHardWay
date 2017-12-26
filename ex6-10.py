# # Lesson 6: Strings and Text
#
# # Define variable x along with number variable
# x = "There are %d types of people." % 10;
#
# # Define string with single quotes
# binary = 'binary';
#
# # Define string with double quotes
# do_not = "don't";
#
# # Define variable of type string with string variables
# y = "Those who know %s and those who %s." % (binary, do_not);
#
# # Print x and y
# print x;
# print y;
#
# # Print string with variables
# print "I said %r." % x;
# print "I also said '%s'." % y;
#
# # Set variables
# hilarious = False;
# joke_evaluation = "Isn't that joke funny?! %r";
#
# # Print variables
# print joke_evaluation % hilarious;
#
# # Set variables
# w = "This is the left side of...";
# e = "a string with a right side.";
#
# # Concatenate variables
# print w + e;



#############



# # Exercise 7: More Printing
#
# print "Mary had a little lamb.";
#
# # Print string including string-variable
# print "Its fleece was white as %s." % 'snow';
# print "And everywhere that Mary went.";
#
# # Print 10 periods/dots
# print "." * 10; # what do you do here?
#
# end1 = 'C';
# end2 = 'h';
# end3 = 'e';
# end4 = 'e';
# end5 = 's';
# end6 = 'e';
# end7 = 'B';
# end8 = 'u';
# end9 = 'r';
# end10 = 'g';
# end11 = 'e';
# end12 = 'r';
#
# # watch that comma at the end. try removing it to see what happens...
#
# #Concatenation
# print end1 + end2 + end3 + end4 + end5 + end6,
# print end7 + end8 + end9 + end10 + end11 + end12



#########



# # Lesson 8: Printing, Printing
#
# formatter = "%r %r %r %r";
#
# print formatter % (1, 2, 3, 4);
# print formatter % ('one', 'two', 'three', 'four');
# print formatter % (True, False, False, True);
# print formatter % (formatter, formatter, formatter, formatter)
# print formatter % (
#     "I had this thing",
#     "That you could type up right.",
#     "But it didn't sing",
#     "So I said goodnight."
# )



##########



# # Exercise 9: Printing, Printing, Printing
#
# # Spaces
# days = "Mon Tes Wed Thu Fri Sat Sun";
#
# # New-line Character: /n
# months = "\nJan\nFeb\nMar\nApr\nMay\nJune\nJuly\Aug\nSept\nOct\nNov\nDec";
#
# # Print string with variable
# print "Days of the week: ", days;
# print "Months of the year: ", months;
#
# # Print multi-line string using 3 double-quotes
# print """
#     There's something going on here with three double quotes.
#     We'll be able to type as much as we want.
#     We can type as many lines as we want...
#     and it will all print out just fine!
# """



###########



# Exercise 10: What Was That?

tabby_cat = "\tI'm tabbed in."; # Tab in
persian_cat = "I'm split\non a line."; # New line
backslash_cat = "I'm \\ a \\ cat."; # Escape backslash

fat_cat = '''
    I'll do a list:
    \t* Cat food
    \t* Fishies
    \t* Catnip\n\t* Grass
'''

print tabby_cat;
print persian_cat;
print backslash_cat;
print fat_cat;

# Escaping similar (single or double) quotes:
say_hello = 'In this string I\'m saying \'Hello!\'';
print say_hello;

# Vertical Tab:
vertical_tab = "Hello there...my name \vis Joey...it's nice to \vmeet you!";
print vertical_tab;

# While Loop - Crashing Editor!
# while True:
#     for i in ["/","-","|","\\","|"]:
#         print "%s\r" % i,
