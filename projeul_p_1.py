# Project Euler problem 1
# Add all of the natural numbers below 1000 that are multiples of 3 or 5.
import time
from functools import reduce

# Took this as an opportunity to test the relative speeds of various
# approaches, including silly ones, like building addition strings and
# eval-ing them.

#max_num = 1000

# 1000 is too small of a number to show any significant differences,
# so I've upped the boundary to 10000. That breaks the silly
# string-building approaches with recursion depth overruns, though.

max_num = 10000

start = time.time()
mult_list = []
print("Build a list with append, and sum it")
for i in list(range(1,max_num)):
    if i % 3 == 0 or i % 5 == 0:
        mult_list.append(i)

print(sum(mult_list))
print(time.time() - start)

print("Build a list, filter it with filter(), and sum it")
start = time.time()
print(sum(filter(lambda x: x%3==0 or x%5==0, range(1,max_num))))
print(time.time() - start)

try:
    print("Build a string of numbers separated by '+' signs and eval it")
    start = time.time()
    print(eval('+'.join(map(str, filter(lambda x:x%3==0 or x%5==0, range(1,max_num))))))
    print(time.time() - start)
except:
    pass

print("Build a list with a list comprehension and sum it")
start = time.time()
print(sum([x if x%3==0 or x%5== 0 else 0 for x in range(1,max_num)]))
print(time.time() - start)

try:
    print("Build an addition string with a list comprehension and eval it")
    start = time.time()
    print(eval('+'.join(map(str, [x if x%3==0 or x%5==0 else 0 for x in list(range(1,max_num))]))))
    print(time.time() - start)
except:
    pass

print("Build a list with a filter and reduce it with a lambda expression")
start = time.time()
print(reduce((lambda x,y: x + y), filter(lambda x: x%3==0 or x%5==0, range(1,max_num))))
print(time.time() - start)
