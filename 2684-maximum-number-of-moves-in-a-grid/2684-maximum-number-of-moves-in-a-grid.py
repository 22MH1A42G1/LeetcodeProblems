class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n, dirs = len(grid), len(grid[0]), [(0, 1), (1, 1), (-1, 1)]
        @cache
        def dp(i, j):
            ans = 0
            for x, y in dirs:
                ni, nj = i + x, j + y
                if 0 <= ni < m and nj < n and grid[i][j] < grid[ni][nj]:
                    ans = max(ans, 1 + dp(ni, nj))
            return ans
        return max(dp(i, 0) for i in range(m))
            