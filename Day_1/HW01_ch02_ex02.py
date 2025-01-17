# HW01_ch02_ex02
# NOTE: You do not run this script.
# #
# Practice using the Python interpreter as a calculator.
# Paste answer and calculations below

# 1. The volume of a sphere with radius r is 4/3 π r^3.
# What is the volume of a sphere with radius 5? [523.5987755982989]
>>> r = 5
>>> from math import pi
>>> volume = (4*pi*r*r*r)/3
>>> volume
#523.5987755982989

# 2. Suppose the cover price of a book is $24.95, but bookstores get a
# 40% discount. Shipping costs $3 for the first copy and 75 cents for
# each additional copy. What is the total wholesale cost for 60 copies?
# total wholesale cost: [646.05]
>>> total_cost = (24.95*60*60)/100
>>> total_cost_with_shipping = total_cost +3 + (0.75*59)
>>> total_cost_with_shipping
945.45

# 3. If I leave my house at 6:52 am and run 1 mile at an easy pace
# (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy
# pace again, what time do I get home for breakfast?
# time: 7:30 AM
>>> total_time = (2*(8+(15/60))) + (3*(7+(12/60)))
>>> total_time
38.1
