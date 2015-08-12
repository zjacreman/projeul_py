# Project Euler problem 21
# Find the sum of all amicable numbers under 10000

# Where an amicable number is part of an amicable pair

# Where an amicable pair is such that all of the proper divisors (the
# set of all divisors except for the number itself) of a number x add
# up to a second number y, and all of the proper divisors of that
# second number y add up to the first number, x.

def find_prop_divisors(num):
    """Returns a list of num's proper divisors"""
    divs = []
    sqrt = int(num**.5) + 1
    for i in range(1, sqrt):
        if num % i == 0:
            divs.append(i)
            if i != 1 and (num // i) not in divs:
                divs.append(num // i)
    return divs

def sum_divisors(num):
    return sum(find_prop_divisors(num))

amicables = []

for i in range(2, 10000):
    x = sum_divisors(i)
    if sum_divisors(x) == i and x != i:
        if i not in amicables:
            amicables.append(i)
        if x not in amicables:
            amicables.append(x)

print(amicables)
print(sum(amicables))
    
        
