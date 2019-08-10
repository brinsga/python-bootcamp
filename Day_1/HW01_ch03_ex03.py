#!/usr/bin/env python
# HW02_ch03_ex03

# This exercise can be done using only the statements and other features we
# have learned so far.

# (1) Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +

# Hint: to print more than one value on a line, you can print a
# comma-separated sequence of values:

# print('+', '-')

# By default, print advances to the next line, but you can
# override that behavior and put a space at the end, like this:

# print('+', end=' ')
# print('-')

# The output of these statements is '+ -'.

# A print statement with no argument ends the current line and
# goes to the next line.


# (2) Write a function that draws a similar grid with four rows and four
# columns.
###############################################################################
# Write your functions below:
# Body
i = 0
a = '+ '
b = '- '
c = '| '
d = '  '


def big_grid():
	""" This function prints a big square grid 11*11 pattern
	"""
	for i in range(11):
		for j in range(11):
			if i%5 == 0 and j%5 == 0:
				print(a, end="")
			elif i%5 != 0 and j%5 == 0:
				print (c, end="")
			elif i%5 == 0 and j%5 != 0:
				print (b, end="")
			else:
				print (d, end="")
		print('')


def small_grid():
	""" This function builds a small 4*4 square grid pattern
	"""
	for i in range(4):
		for j in range(4):
			if i%3 == 0 and j%3 == 0:
				print(a,end="")
			elif i%3 != 0 and j%3 == 0:
				print (c, end="")
			elif i%3 == 0 and j%3 != 0:
				print (b, end="")
			else:
				print (d, end="")
		print('')


# Write your functions above:
###############################################################################
def main():
    """Call your functions within this function.
    When complete have two function calls in this function:
    two_by_two()
    four_by_four()
    """
    print('This is the BIG GRID')
    big_grid()
    print('This is the SMALL GRID')
    small_grid()

if __name__ == "__main__":
    main()
