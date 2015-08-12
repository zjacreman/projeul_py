# Project Euler problem 2
# Find the sum of all the even-numbered Fibonacci terms
# less than 4,000,000.
import time

def find_even_fib_terms(max_fib):
    fibs = [0, 1, 1]
    while fibs[-1] < max_fib:
        fibs.append(fibs[-1] + fibs[-2])

    def _is_even_and_less_than_max(num):
        return num % 2 == 0 and num < max_fib
    return filter(_is_even_and_less_than_max, fibs)

print("Higher-resource method, with lists and filtering")
start = time.time()
even_fibs = find_even_fib_terms(4000000)
print(sum(even_fibs))
print(time.time() - start)


# That was a little unnecessarily silly. More straightforward state
# variable approach, no extra listing or summing req'd.

def find_total_of_even_fib_terms_low_footprint(max_fib):
    total = 0
    fib1 = 1
    fib2 = 1
    while fib2 < max_fib:
        temp_fib = fib1 + fib2
        if temp_fib % 2 == 0 and temp_fib < max_fib:
            total += temp_fib
        fib1 = fib2
        fib2 = temp_fib
    return total

print("Low-resource method, with state variables")
start = time.time()
print(find_total_of_even_fib_terms_low_footprint(4000000))
print(time.time() - start)
