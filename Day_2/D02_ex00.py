#!/usr/bin/env python3
# D04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program

# Please write a docstring for every function you write.

###############################################################################
# Imports
import random

# Body

def guess_game():
	number = random.randint(1,25)
	for i in range(1,6):
		while True:
			try:
				guess = int(input("Enter a number between 1 and 25"))
				break
			except ValueError:
				print(" Please enter a number between 1 and 25")
		if guess == number:
			print(" Your guess is right")
			break
		elif guess > number:
			print("Your guess is high")
		else:
			print("Your guess is low")
		if i == 5:
			print("You have exceeded the maximum limit")

	


###############################################################################
def main():
    guess_game()  # Remove this and replace with your function calls


if __name__ == '__main__':
    main()
