# Project Euler problem 4
# Find the largest palindrome made from the product of two 3-digit numbers.
import time
start = time.time()
results = []
for x in range(999, 900, -1):
    for y in range(999, 900, -1):
        teststr = str(x*y)
        revstr = teststr[::-1]
        if teststr == revstr and (x*y) not in results:
            results.append(x*y)
print(max(results))
end = time.time() - start
print(end)
