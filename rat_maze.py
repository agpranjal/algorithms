def solve(grid, i=0, j=0):
    global ans

    if grid[i][j] == 0:
        return
    
    if i == len(grid)-1 and j == len(grid)-1 and grid[i][j] == 1:
        return True

    if i+1 < len(grid):
        sol[i+1][j] = "*"

        if solve(grid, i+1, j):
            return True

        sol[i+1][j] = 0

    if j+1 < len(grid):
        sol[i][j+1] = "*"
        if solve(grid, i, j+1):
            return True
        sol[i][j+1] = 0

    return False



grid = [
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 1]
    ]

sol = []
for i in range(len(grid)):
    sol.append([0]*len(grid))
sol[0][0] = "*"

if solve(grid):
    for i in range(len(sol)):
        print(*sol[i])
else:
    print("No solution")
