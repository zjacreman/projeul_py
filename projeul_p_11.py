# Project Euler problem 11
# In a 20x20 grid, find the largest product of four numbers in a straight line.

# Initialize the arrays
GRID = []
f = open("projeul_p_11.txt")
for line in f:
    GRID.append(list(map(int, line.split())))
f.close()

OFFSET = 3

inc = lambda x,y: x + y
dec = lambda x,y: x - y
zero = lambda x,y: x

# Define helper function
def prod(r, c, rfun, cfun):
    try:
        product = 1
        for add in range(OFFSET + 1):
            product *= GRID[rfun(r, add)][cfun(c, add)]
        return product
    except:
        return 0

max_product = 0

for row_i in range(len(GRID)):
    for col_i in range(len(GRID)): # Assumes a square GRID
        max_product = max(prod(row_i, col_i, zero, inc), max_product)
        max_product = max(prod(row_i, col_i, inc, zero), max_product)
        max_product = max(prod(row_i, col_i, inc, inc), max_product)
        max_product = max(prod(row_i, col_i, inc, dec), max_product)

print(max_product)
