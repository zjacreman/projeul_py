# Project Euler problem 10
# Sum of all primes below 2 million

# Gonna use the Sieve of Eratosthenes.
import time

MAX = 2000000
start = time.time()
candidates = list(range(MAX))
fin = int(MAX**.5)
for i in range(2, fin + 1):
    if candidates[i]:
        candidates[i**2::i] = [0] * len(candidates[i**2::i]) # with 0, no need to filter before summing
print(sum(candidates[2:]))
print(time.time() - start)
