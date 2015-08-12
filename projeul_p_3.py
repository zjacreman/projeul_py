# Project Euler problem 3
# Find the largest prime factor of 600851475143

def find_prime_factors(num):
    factors = []
    div = 2
    while num > 1:
        while num % div == 0:
            factors.append(div)
            num //= div
        div += 1
        if div**2 > num:
            if num > 1:
                factors.append(num)
            break
    return factors            

import time
start = time.time()
prime_factors = find_prime_factors(600851475143)
end = time.time() - start
print(max(prime_factors))
print(end)

print(prime_factors)


