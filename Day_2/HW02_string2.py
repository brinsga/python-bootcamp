#!/usr/bin/env python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises


# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
    """ The function accepts a string as arguments and adds 'ing' to the 
    end if the string's length is greater than 3 and does not end with 'ing'.
    If the string ends witn 'ing', then 'ing' is removed and 'ly' is added. 
    And if the length is less than 3, the string is left unchanged
    """
    leng = len(s)
    if leng < 3:
        return s
    elif s[(leng-3):leng] == 'ing':
        return s[0:leng] + 'ly'
    else: 
        return s + 'ing'

    
# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
    index_1 = s.find('not')
    index_2 = s.find('bad')
    if index_1 > index_2 :
        return s
    else:
        replaced_str = s.replace(s[index_1:(index_2+3)], 'good' ,1)
        return replaced_str


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
    def dividing_string(n):
        leng = len(n)
        if leng % 2 == 0:
            n_front = n[0:(leng//2)]
            n_back = n[leng//2:leng]
            return n_front, n_back
        else: 
            n_front = n[0:((leng//2)+1)]
            n_back = n[((leng//2)+1):len(n)]
            return n_front,n_back
    a_front, a_back = dividing_string(a)
    b_front, b_back = dividing_string(b)
    return a_front + b_front + a_back + b_back





# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print()
    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print()
    print('front_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')


if __name__ == '__main__':
    main()
