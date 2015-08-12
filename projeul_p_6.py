# Project Euler problem 6
# What is the difference between the sum of the squares and the
# square of the sums of the first 100 natural numbers?

def sum_of_squares(num):
    _sum = 0
    for i in range(1, num + 1):
        _sum += i**2
    return _sum

def square_of_sums(num):
    _sum = 0
    for i in range(1, num + 1):
        _sum += i
    return _sum**2

import time
start = time.time()
print(square_of_sums(100) - sum_of_squares(100))
print(time.time()-start)
