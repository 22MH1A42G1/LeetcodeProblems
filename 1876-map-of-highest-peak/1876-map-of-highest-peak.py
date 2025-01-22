from typing import List
from collections import deque

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows, cols = len(isWater), len(isWater[0])
        heights = [[-1] * cols for _ in range(rows)]
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if isWater[i][j] == 1:
                    heights[i][j] = 0
                    queue.append((i, j))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and heights[nx][ny] == -1:
                    heights[nx][ny] = heights[x][y] + 1
                    queue.append((nx, ny))
        return heights
