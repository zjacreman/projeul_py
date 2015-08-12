# Project Euler, problem 5
# What is the smallest number divisible by each of the numbers 1-20?
import time
from functools import reduce

def find_prime_factors(num):
    """
    Does what it says on the tin. 
    """
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

def find_max_prime_factor(prime_factor_lists):
    """
    Given a list of lists of prime factors, find the biggest prime
    factor in the whole dang mess.
    """
    max_factor = 1
    for l in prime_factor_lists:
        try:
            if max(l) > max_factor:
                max_factor = max(l)
        except:
            pass
    return max_factor

def build_supreme_prime_factor_list(prime_factor_lists):
    """
    Given a list of lists of prime factors, consolidate them all
    into a single list containing the maximum number of occurrences
    of each prime factor.

    Ex: [[2],[2,2,2],[2,2,3]] -> [2,2,2,3]
    """
    factor_list = []
    max_factor = find_max_prime_factor(prime_factor_lists)
    for l in prime_factor_lists:
        for i in range(2, max_factor + 1):
            if l.count(i) > factor_list.count(i):
                factor_list += [i]*(l.count(i)-factor_list.count(i))
    return sorted(factor_list)

start = time.time()
prime_factor_lists = []

for i in range(1,21):
    prime_factor_lists.append(find_prime_factors(i))

supreme_prime_factors = build_supreme_prime_factor_list(prime_factor_lists)

print(reduce((lambda x,y: x*y), supreme_prime_factors))
print(time.time() - start)
