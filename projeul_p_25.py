# Project Euler problem 25
# First fibonacci term to contain 1000 digits

import time
start = time.time()
f_n_minus_two = 1
f_n_minus_one = 1
n = 3

while True:
    f_n = f_n_minus_two + f_n_minus_one
    if len(str(f_n)) == 1000:
        break
    else:
        f_n_minus_two = f_n_minus_one
        f_n_minus_one = f_n
        n += 1
print(f_n, n)
print(time.time() - start)
