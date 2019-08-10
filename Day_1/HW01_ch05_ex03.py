#!/usr/bin/env python
# HW02_ch05_ex03

# If you are given three sticks, you may or may not be able to arrange them in
# a triangle. For example, if one of the sticks is 12 inches long and the other
# two are one inch long, it is clear that you will not be able to get the short
# sticks to meet in the middle. For any three lengths, there is a simple test
# to see if it is possible to form a triangle:

#   If any of the three lengths is greater than the sum of the other two, then
#   you cannot form a triangle. Otherwise, you can. (If the sum of two lengths
#   equals the third, they form what is called a "degenerate" triangle.)

# (1) Write a function named `is_triangle` that takes three integers as
# arguments, and that prints either "Yes" or "No," depending on whether you can
# or cannot form a triangle from sticks with the given lengths.

# (2) Write a function that prompts the user to input three stick lengths,
# converts them to integers, and uses `is_triangle` to check whether sticks
# with the given lengths can form a triangle.

###############################################################################
# Write your functions below:
# Body

def is_triangle(x,y,z):
    """ is_triangle function is given three lengths as arguments and is used to 
    find if a triangle can be formed out of them
    """
    maxi = max(x,y,z)
    if maxi <= (x+y+z-maxi):
        return 'Yes'
    else:
        return 'No'


def check_stick_lengths():
    """
    The function predicts whether a triangle can be formed based on three inputs 
    from the user
    """
    x = []
    i=0
    while i<3:
        while True:
            try:
                number = int(input("Enter a side of triangle"))
                break
            except ValueError:
                print("Oops. Please enter a integer value")
        x.append(number)
        i = i+1
    length_check = is_triangle(x[0],x[1],x[2])
    return length_check


# Write your functions above:
###############################################################################
def main():
    """Call your functions within this function.
    When complete have four function calls in this function
    for is_triangle (we want to test the edge cases!):
    is_triangle(1,2,3)
    is_triangle(1,2,4)
    is_triangle(1,5,3)
    is_triangle(6,2,3)
    and a function call for
    check_stick_lengths()
    """
    print(is_triangle(1,2,3))
    print(is_triangle(1,2,4))
    print(is_triangle(1,5,3))
    print(is_triangle(6,2,3))
    outp = check_stick_lengths()
    print(outp)
    
if __name__ == "__main__":
    main()
