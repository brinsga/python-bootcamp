#!/usr/bin/env python
# HW02_ch05_ex02

# Fermat's Last Theorem says that there are no positive integers a, b, and c
# such that
#        a^n + b^n = c^n
# for any values of n greater than 2.

# (1) Write a function named `check_fermat` that takes four parameters-a, b, c
# and n-and that checks to see if Fermat's theorem holds. If n is greater than
# 2 and it turns out to be true that
#        a^n + b^n = c^n
# the program should print, "Holy smokes, Fermat was wrong!""
# Otherwise the program should print, "No, that doesn't work."

# (2) Write a function named `check_fermat_ints` that prompts the user to input
# values for a, b, c and n, converts them to integers, and uses check_fermat
# to check whether they violate Fermat's theorem.

###############################################################################
# Write your functions below:
# Body


def check_fermat(a,b,c,n):
  	""" The function checks if the fermat theorem holds true for n > 2

  	"""
  	if n<=2:
  		print ('Fermats theorem cannot be computed')
  	elif a**n + b**n == c**n :
  		print ('Holy Smokes, Fermat was wrong')
  	else:
  		print('No, that doesnt work')

def check_fermat_ints():
	def check_input(message):
		while True:
			try:
				inp = int(input(message))
			except Valueerror:
				print('Please provide an integer')
			return inp
	a = check_input('Enter the value of a : ')
	b = check_input('Enter the value of b : ')
	c = check_input('Enter the value of c : ')
	n = check_input('Enter the value of n as greater than 2 : ')
	check_fermat(a,b,c,n)


# Write your functions above:
###############################################################################
def main():
    """Call your function within this function.
    When complete have one function call in this function:
    check_fermat_ints(1,2,3,4)
    and two functions defined in the body:
    check_fermat_ints()
    check_fermat()

    """
    check_fermat_ints()

if __name__ == "__main__":
    main()
