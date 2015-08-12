# Project Euler problem #48
# Find the last 10 digits of 1**1 + 2**2 + ... + 1000 ** 1000

# This one was so easy (thanks Python!) that it felt like cheating.
# Some day I'm going to come back to these in a language with no big
# number support.
# I don't feel proud of this one. I actually just typed it into the
# interpreter and made up this document afterward for posterity.
import time
start = time.time()
total = 0
for i in range(1, 1001):
    total += i ** i
print(str(total)[-10:])
print(time.time() - start)

# Alternative one-liner list comprehension
start = time.time()
print(str(sum([i ** i for i in range(1, 1001)]))[-10:])
print(time.time() - start)
