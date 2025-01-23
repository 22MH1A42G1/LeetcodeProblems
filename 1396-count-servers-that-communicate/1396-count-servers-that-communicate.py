class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        r = [sum(w) for w in grid]
        c = [sum(grid[i][j] for i in range(len(grid))) for j in range(len(grid[0]))]
        return sum(1 for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j]==1 and (r[i]>1 or c[j]>1))
