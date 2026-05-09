class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        min_len = min(m, n) // 2
        ans = [row[:] for row in grid]

        for l in range(min_len):
            r, c, v = [], [], []
            for i in range(l, m - l - 1):
                r.append(i)
                c.append(l)
                v.append(grid[i][l])
            for j in range(l, n - l - 1):
                r.append(m - l - 1)
                c.append(j)
                v.append(grid[m - l - 1][j])
            for i in range(m - l - 1, l, -1):
                r.append(i)
                c.append(n - l - 1)
                v.append(grid[i][n - l - 1])
            for j in range(n - l - 1, l, -1):
                r.append(l)
                c.append(j)
                v.append(grid[l][j])

            t = len(v)
            km = k % t
            for i in range(t):
                ans[r[i]][c[i]] = v[(i - km) % t]
        return ans