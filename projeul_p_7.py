# Project Euler Problem #7
# What is the 10001st prime number?
import time
start = time.time()
found_primes = [2, 3, 5, 7, 11, 13] # given in problem
candidate = found_primes[-1] + 2

while len(found_primes) < 10001:
    is_prime = True
    for prime in found_primes:
        if prime > (candidate**.5):
            break
        if candidate % prime == 0:
            is_prime = False
            break
    if is_prime:
        found_primes.append(candidate)
    candidate += 2
print(found_primes[-1], len(found_primes))
print(time.time()-start)
