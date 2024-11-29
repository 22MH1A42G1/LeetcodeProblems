class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1: return -1
        m, n = len(grid), len(grid[0])
        visited = set()
        pq = [(grid[0][0], 0, 0)]
    
        while pq:
            time, row, col = heappop(pq)
            if row == m-1 and col == n-1: return time
            if (row, col) in visited: continue
            visited.add((row, col))
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                r, c = row + dr, col + dc
                if 0 <= r < m and 0 <= c < n and (r, c) not in visited:
                    wait = 1 if ((grid[r][c] - time) % 2 == 0) else 0
                    heappush(pq, (max(time + 1, grid[r][c] + wait), r, c))