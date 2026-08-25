# Q19. Minimum Cost Path using Dynamic Programming

def minimum_cost_path(grid):
    n = len(grid)
    m = len(grid[0])

    # Create DP table
    dp = [[0] * m for _ in range(n)]

    # Starting cell
    dp[0][0] = grid[0][0]

    # First row
    for j in range(1, m):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    # First column
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    # Fill remaining cells
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = grid[i][j] + min(
                dp[i - 1][j],       # Up
                dp[i][j - 1],       # Left
                dp[i - 1][j - 1]    # Diagonal
            )

    return dp[n - 1][m - 1], dp


# Input
grid = [
    [1, 2, 3],
    [4, 8, 2],
    [1, 5, 3]
]

# Find minimum cost
minimum_cost, dp = minimum_cost_path(grid)

# Output
print("Cost Matrix:")
for row in grid:
    print(*row)

print("\nDP Table:")
for row in dp:
    print(*row)

print("\nMinimum Cost =", minimum_cost)
