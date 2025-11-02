class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        for x, y in walls + guards:
            grid[x][y] = 2
        for guard_x, guard_y in guards:
            for dx, dy in [(-1,0), (0,1), (1,0), (0,-1)]:
                x, y = guard_x, guard_y
                while True:
                    x += dx
                    y += dy
                    if x < 0 or x >= m or y < 0 or y >= n:
                        break                  
                    if grid[x][y] == 2:
                        break
                    grid[x][y] = 1
        unguarded = 0
        for row in grid:
            unguarded += row.count(0)
        return unguarded