#!/usr/bin/env python3
# HW04_ch08_ex00
# See 8.7

# The following program counts the number of times the letter 'a' appears in a
# string:

#     word = 'banana'
#     count = 0
#     for letter in word:
#         if letter == 'a':
#             count = count + 1
#     print(count)

# Encapsulate this code in a function named "count", and generalize it so that
# it accepts the string and the letter as arguments.

# Please write a docstring for every function you write.

###############################################################################
# Imports

def count(word,match_letter):
	""" The function count takes in a string and a character as an input and computes
	the number of times the character appears in a string.

	"""
	count = 0
	for letter in word:
		if letter == match_letter:
			count = count +1
	print(count)


# Body


###############################################################################
def main():

    # Remove print("Hello World!") and add several functions calls to count()
    # below, passing various strings and letters
    count('apple','a')
    count('keek keek','e')
    count('hoot toot','t')

if __name__ == '__main__':
    main()
