from collections import deque
from typing import List
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 0: return 0
        id_grid = [[-1] * n for _ in range(n)]
        island_sizes = {}
        current_id = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and id_grid[i][j] == -1:
                    queue = deque()
                    queue.append((i, j))
                    id_grid[i][j] = current_id
                    size = 1
                    while queue:
                        x, y = queue.popleft()
                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1 and id_grid[nx][ny] == -1:
                                id_grid[nx][ny] = current_id
                                queue.append((nx, ny))
                                size += 1
                    island_sizes[current_id] = size
                    current_id += 1
        max_size = max(island_sizes.values()) if island_sizes else 0
        result = max_size
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    neighbors = set()
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                            neighbors.add(id_grid[nx][ny])
                    total = 1  
                    for island_id in neighbors:
                        total += island_sizes[island_id]
                    if total > result:
                        result = total
        return result