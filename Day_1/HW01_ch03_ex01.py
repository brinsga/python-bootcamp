#!/usr/bin/env python
# HW02_ch03_ex01

# Python provides a built-in function called len that returns the length
# of a string, so the value of len('monty') is 5.

# Write a function named `right_justify` that takes a string named `s` as a
# parameter and prints the string with enough leading spaces so that the
# last letter of the string is in column 70 of the display.

# Example:
# >>> right_justify('monty')
#                                                                  monty
###############################################################################
# Write your function below:
# Body
def right_justify(s):
	""" The function right justify by adding leading spaces to the string s and 
	displays the last letter of the string in the 70th column of the display.
	"""
	adjustment = 70 - len(s)
	print(' '*adjustment + s)


# Write your function above:
###############################################################################
def main():
    """Call your functions within this function."""

    right_justify("Python")
    right_justify("Brinda Gurusamy")


if __name__ == "__main__":
    main()
