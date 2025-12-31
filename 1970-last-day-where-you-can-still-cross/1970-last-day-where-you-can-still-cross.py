class Solution:
    def canCross(self,row,col,cells,day):
            grid=[[0]*col for _ in range(row)]
            for i in range(day):
                r, c = cells[i]
                grid[r-1][c-1]=1
            queue = deque()
            visited = set()
            for c in range(col):
                if grid[0][c]==0:
                    queue.append((0,c))
                    visited.add((0,c))
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            while queue:
                r, c = queue.popleft()
                if r == row - 1:
                    return True
                for dr, dc in directions:
                    nr,nc = r+dr,c+dc
                    if 0<=nr<row and 0<=nc<col and grid[nr][nc]==0 and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        queue.append((nr,nc))
            return False
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        left, right = 1, len(cells)
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if self.canCross(row,col, cells, mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans 