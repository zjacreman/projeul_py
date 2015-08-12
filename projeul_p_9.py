# Project Euler problem #9
# Find the only Pythagorean triplet {a, b, c] for which
# a + b + c = 1000.
# (Actually, find the product of a, b, and c)
import time

start = time.time()
found = False
for a in range(1, 1001):
    if found: break
    for b in range(1, 1001 - a):
        if found: break
        c = 1000 - a - b
        if c**2 == a**2 + b**2:
            found = True
            print(a, b, c, a * b * c)

print(time.time() - start)
