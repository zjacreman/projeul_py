# Project Euler problem 30
# Find the sum of all numbers that can be written as the sum of fifth
# powers of their digits.
# For example, 1634 = 1**4 + 6**4 + 3**4 + 4**4

winners = []
for i in range(2, 354294 + 1): # (9**5) * 6; (9**5) * 7 is still a
                                # 6-digit number, meaning that after 6
                                # digits summing the fifth power of 9
                                # can't even approach the number being
                                # tested. Therefore, 354294 is as
                                # large as they're going to get.
    intstr = str(i)
    subtotal = 0
    for char in intstr:
        subtotal += int(char) ** 5
    if subtotal == i:
        winners.append(i)

print(sum(winners))
        
