# Project Euler problem 13
# Find the 1st ten digits of the sum of 100 50-digit numbers
# Given in projeul_p_13_numbers.txt

# Python's bignum support makes this totally trivial.
f = open('projeul_p_13_numbers.txt')
sum = 0
for line in f:
    sum += int(line)
print(sum, len(str(sum)))
print(str(sum)[:10])
