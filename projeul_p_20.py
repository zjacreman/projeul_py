# Project Euler problem #20
# Sum the digits in 100!


# This one is completely trivial.

import math
total = 0
numstr = str(math.factorial(100))
for char in numstr:
    total += int(char)
print(total)

