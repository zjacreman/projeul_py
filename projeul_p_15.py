# Project Euler problem 15
# How many routes from the top left to bottom right of a 20x20 grid?

# instantiate 20x20 grid
GRID = []
for _ in range(20):
    GRID.append([0]*20)

# OK. So I'm going to do a few things here; first, I'm going to
# consider the route as going from top right to bottom left, because
# it makes the programming a little more straightforward. Second, I'm
# going to point out that when your path has reached the upper-right
# corner of the lower-left most square - (1,1) on a cartesian grid -
# there are only two possible routes to take. So I'm going to put a 2
# in the array space [0][0].

GRID[0][0] = 2

# If you look at cartesian (2, 1), from there you can only find 3
# routes to origin. And likewise at (1, 2). That is, the two routes to
# origin from (1,1), and one route that doesn't pass through (1,1). As
# you move out along the lowest row and up the leftmost column, the
# number of available routes increases by one each time.

for i in range(1,20):
    GRID[0][i] = GRID[0][i-1] + 1
    GRID[i][0] = GRID[i-1][0] + 1

# Now, if you add [0][1] and [1][0] together, you get 6, or the total
# number of routes possible in a 4x4 square. At [1][1], there are 3
# possible routes in one move direction, and 3 in the other; 6 total
# subroutes.

GRID[1][1] = 6

# From these principles - adding adjacent subroute totals - you can
# work backwards to the upper-right corner, from whence the most
# possible subroutes available. Since no backtracking is allowed,
# number of possible subroutes are mirrored across the diagonal axis
# of the grid.

for x in range(2, 20):
    for y in range(1, 20):
        GRID[x][y] = GRID[x][y-1] + GRID[x-1][y]
        GRID[y][x] = GRID[x][y]


# When we're done, [19][19] has the total number of subroutes.
print(GRID[19][19])

# It turns out you can get a value in the central line of Pascal's Triangle
# by simply dividing (2n)! / (n! * n!), but I didn't learn this until later.
