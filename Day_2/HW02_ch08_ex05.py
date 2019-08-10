# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 5 for the task.
# Please do provide function calls that test/demonstrate your
# function.
# Please write a docstring for every function you write.
def rotate_word(name, shift):
	""" Function to rotate each character of a string based on a shift number(Caesar Cipher)
	"""

	def case(s,shift,start,end):
		"""Function to calculate the characteristics of each character and evaluate the shift individually
		"""
		if ord(s)+shift > end:
			return chr(ord(s)+shift-26)
		elif ord(s)+shift < start:
			return chr(ord(s)+shift+26)
		else:
			return chr(ord(s)+shift)
	result = ''

	for c in name:
		if c.islower():
			result += case(c,shift,97,122)
		elif c.isupper():
			result += case(c,shift,65, 90)
		else:
			result += c

	return result

def main():
	cipher1 = rotate_word('cheer',7)
	cipher2 = rotate_word('melon', -10)
	cipher3 = rotate_word('sleep',9)
	cipher4 = rotate_word('abc#d',1)
	print(cipher1,cipher2,cipher3,cipher4)

if __name__ == '__main__':
	main()


