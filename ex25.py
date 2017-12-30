# Exercise 25: More Practice (calling functions within functions)

def break_words(stuff):
    # Breaks on space and stores in array
    words = stuff.split(' ')
    # Returns array of words
    return words

def sort_words(words):
    # Sorts words in alphabetical order
    return sorted(words)

def print_first_word(words):
    word = words.pop(0)
    print word

def print_last_word(words):
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


# # Result:

# Enter Python
# python

# Python 2.7.12 (default, Nov 20 2017, 18:23:56)
# [GCC 5.4.0 20160609] on linux2
# Type "help", "copyright", "credits" or "license" for more information.

# Import the script
# >>> import ex25

# Define variable 'sentence'
# >>> sentence = "All good things come to those who wait!"

# Pass 'sentence' into the break_words() function
# >>> words = ex25.break_words(sentence)

# Print the returned value from break_words() -> array
# >>> words
# ['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait!']

# Pass 'words' variable to the sort_words() function and store in new variable 'sorted_words'
# >>> sorted_words = ex25.sort_words(words)

# Print the returned value from sort_words() function
# >>> sorted_words
# ['All', 'come', 'good', 'things', 'those', 'to', 'wait!', 'who']

# Pass 'words' variable to print_first_word() function
# >>> ex25.print_first_word(words)
# All

# Pass 'words' variable to print_last_word() function
# >>> ex25.print_last_word(words)
# wait!

# Print words -> notice 'wait' has been poped (removed) from the array!
# >>> words
# ['good', 'things', 'come', 'to', 'those', 'who']

# Pass 'sorted_words' variable to print_first_word() function
# >>> ex25.print_first_word(sorted_words)
# All

# Pass 'sorted_words' variable to print_last_word() function
# >>> ex25.print_last_word(sorted_words)
# who

# Print 'sorted_words' variable -> notice 'who' has been poped (removed) from the array!
# >>> sorted_words
# ['come', 'good', 'things', 'those', 'to', 'wait!']

# Redifine 'sorted_words' variable passing in sentence
# >>> sorted_words = ex25.sort_sentence(sentence)

# Print 'sorted_words' variable
# >>> sorted_words
# ['All', 'come', 'good', 'things', 'those', 'to', 'wait!', 'who']

# Pass 'sentence' to print_first_and_last() function
# >>> ex25.print_first_and_last(sentence)
# All
# wait!

# Pass 'sentence' to print_first_and_last_sorted() function
# >>> ex25.print_first_and_last_sorted(sentence)
# All
# who
