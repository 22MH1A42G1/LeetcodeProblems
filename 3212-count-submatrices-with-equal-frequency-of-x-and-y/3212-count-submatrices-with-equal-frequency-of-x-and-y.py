class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        x = [[0] * (n+1) for _ in range(m+1)]
        y = [[0] * (n+1) for _ in range(m+1)]
        c = 0
        for i in range(m):
            for j in range(n):
                x[i+1][j+1] = x[i][j+1] + x[i+1][j] - x[i][j] + (grid[i][j] == 'X')
                y[i+1][j+1] = y[i][j+1] + y[i+1][j] - y[i][j] + (grid[i][j] == 'Y')
                c += x[i+1][j+1] and x[i+1][j+1] == y[i+1][j+1]
        return c