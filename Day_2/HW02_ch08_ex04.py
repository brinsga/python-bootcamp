#!/usr/bin/env python3
# HW04_ch08_ex04

# The following functions are all intended to check whether a string contains
# any lowercase letters, but at least some of them are wrong. For each
# function, describe (is the docstring) what the function actually does.
# You can assume that the parameter is a string.

# Do not merely paste the output as a counterexample into the documentation
# string, explain what is wrong.


###############################################################################
# Body


def any_lowercase1(s):
    """Every Character from the string is checked if it is in lowercase, if an uppercase letter is encountered as the
    first letter of the string the program returns 'False' even if the consecutive letters are in lower case
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    """'c'.islower condition finds if the character c 'c' is in lower case.  And for every letter in the string, the 
    condition 'c'.islower is evaluated and the result always evaluates to True except when the string is empty.
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    """ The value of flag returned at the end of the function is True if the last letter is lower case and False if
    the last letter is in upper case. Hence the program doesn't compute to find if at least a lower case letters exist"
    """
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    """Explain what is wrong, if anything, here.
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def any_lowercase5(s):
    """When a string begins with an Upper case, the program returns False without computing the subsequent charcters
    and the hence the presence of lower case characters in a string is not recognised.
    """
    for c in s:
        if not c.islower():
            return False
    return True


###############################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong,
    # call that function with a string for which the function returns
    # incorrectly.
    # ex.: any_lowercase_("thisstringmessesupthefunction")
    print("Hello World!")
    print(any_lowercase5("tO"))

if __name__ == '__main__':
    main()
