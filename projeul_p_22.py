# Project Euler problem 22

# Find the total of the name scores for the names in file
# projeul_p_22_names.txt.

# Name score is determined by summing the letter scores ( A -> 1, B ->
# 2, etc.) of each individual letter in the name, and then multiplying
# that by the name's sorted position in the list.

# Example: COLIN's letters are worth 53 pts, times its sorted position
# of 938, yielding 49714.

# Create the letter score dict

import string
LETTER_SCORES = {}
for i, char in enumerate(string.ascii_uppercase):
    LETTER_SCORES[char] = i + 1

# Open the file and get the names out
f = open("projeul_p_22_names.txt")
fstr = f.read()
f.close()

#out = open("projeul_p_22_names_sorted.txt", 'w')

import time
start = time.time()
# Process the names into a sorted list
name_list = sorted(fstr.replace('"','').split(','))

total = 0
for i, name in enumerate(name_list):
    pos = i + 1
    score = 0
    for char in name:
        score += LETTER_SCORES[char]
    total += score * pos
#    out.write(name + '\n')

print(total)
print(time.time() - start)
