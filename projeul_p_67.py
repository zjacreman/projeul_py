# Project Euler problem 67
# Find the maximum total from top to bottom in 100-row triangle

# Load up the triangle
ROWS = []
f = open('projeul_p_67_triangle.txt')
for line in f:
    ROWS.append(line.split())
f.close()

# Initialize memo dictionary
MEMO_DICT = {}

# Implement the decision tree
def find_max_path(row, index):
    if (row, index) not in MEMO_DICT:
        current_pos = int(ROWS[row][index])
        try:
            largest_subpath = max(find_max_path(row + 1, index),
                                  find_max_path(row + 1, index + 1))
            MEMO_DICT[(row, index)] = current_pos + largest_subpath
        except: # current element is at the bottom of the triangle
            MEMO_DICT[(row, index)] = current_pos
    return MEMO_DICT[(row, index)]

print(find_max_path(0, 0)) # Start at the top with an empty memo
