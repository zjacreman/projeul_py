# Project Euler problem 12
# First triangle number to have more than 500 divisors
# Triangle numbers being made by summing consecutive integers, that is
# 1 + 2 + 3 is a triangle number.

# This method is kind of slow, but I am not immediately seeing
# anything better, and it's not so slow that I want to try to find a
# better way.

def count_divisors(num):
    divisors = []
    for i in range(1, int(num**.5) + 1):
        if num % i == 0:
            if i not in divisors:
                divisors.append(i)
            if (num / i) not in divisors:
                divisors.append(num / i)
    return len(divisors)

i = 0
tri_num = 0

while True:
    i += 1
    tri_num += i
    if count_divisors(tri_num) > 500:
        print(tri_num)
        break

