# Project Euler problem 11
# In a 20x20 grid, find the largest product of four numbers in a straight line.

# Initialize the arrays
GRID = []
f = open("projeul_p_11.txt")
for line in f:
    GRID.append(list(map(int, line.split())))
f.close()

OFFSET = 3

inc = lambda x,y: x + y # Increments the row or column by up to OFFSET
dec = lambda x,y: x - y # Decrements the row or column by up to OFFSET
zero = lambda x,y: x    # Leaves row or column alone

# Helper function that applies lambda functions to starting coordinates
def prod(start_row, start_col, row_func, col_func):
    try:
        product = 1
        for add in range(OFFSET + 1):
            product *= GRID[row_func(start_row, add)][col_func(start_col, add)]
        return product
    except: # ran up against a border, product invalid
        return 0

max_product = 0

# Start in upper left corner, move right then down
for row_i in range(len(GRID)):
    for col_i in range(len(GRID)): # Assumes a square GRID
        max_product = max(prod(row_i, col_i, zero, inc), max_product)
        max_product = max(prod(row_i, col_i, inc, zero), max_product)
        max_product = max(prod(row_i, col_i, inc, inc), max_product)
        max_product = max(prod(row_i, col_i, inc, dec), max_product)

print(max_product)
