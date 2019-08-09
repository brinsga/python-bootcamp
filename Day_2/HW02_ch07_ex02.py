#!/usr/bin/env python3
# HW04_ch07_ex02

# The built-in function eval takes a string and evaluates it using the Python
# interpreter.
# For example:

#     >>> eval('1 + 2 * 3')
#     7
#     >>> import math
#     >>> eval('math.sqrt(5)')
#     2.2360679774997898
#     >>> eval('type(math.pi)')
#     <type 'float'>

# Write a function called eval_loop that iteratively prompts the user, takes
# the resulting input and evaluates it using eval, and prints the result.

# It should continue until the user enters 'done', and then return the value of
# the last expression it evaluated.

# Here is an opportunity to use things like `try`, `except`, and/or `finally`.

# Please write a docstring for every function you write.

###############################################################################
# Imports
import math

def eval_loop():
	"""
	The eval_loop function iteratively asks for users to input expressions and evaluates
	them until the user types done. The function then returns the last evaluated value and 
	terminates
	"""
	user_input, eval_user_input = '', ''
	while user_input != 'done':
		while True:
			try: 
				user_input= input('Enter a expression to evaluate')
				if user_input == 'done':
			
					break
				eval_user_input = eval(user_input)
				break
			except NameError:
				print("please enter a valid expression")
			except SyntaxError:
				print("Please enter an expression without special characters")
			except TypeError:
				print(" Please enter an expression without special characters")
		
		print(eval_user_input)
	





# Body


###############################################################################
def main():
	eval_loop()

if __name__ == '__main__':
    main()
