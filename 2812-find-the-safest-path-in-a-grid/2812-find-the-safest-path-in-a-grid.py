class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        N = len(grid)
        queue = collections.deque([])
        visited = set()
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    queue.append((i,j))
                    visited.add((i,j))
        
        directions = (-1,0),(1,0),(0,-1),(0,1)
        
        
        safety = 0
        while queue:
            for i in range(len(queue)):
                row,col = queue.popleft()
                grid[row][col] = safety
                
                for dr,dc in directions:
                    nRow,nCol = row+dr,col+dc
                    if nRow >= 0 and nRow < N and nCol >= 0 and nCol < N and (nRow,nCol) not in visited:
                        queue.append((nRow,nCol))
                        visited.add((nRow,nCol))
            safety +=1
        
        res = sys.maxsize
        heap = []
        visited = set()
        heapq.heappush(heap,(-grid[0][0],0,0))
        
        while heap:
            val,i,j = heapq.heappop(heap)
            visited.add((i,j))
            res = min(res, -val)
            
            if i == N-1 and j == N-1:
                return res
            
            for dr,dc in directions:
                nRow,nCol = i+dr,j+dc
                if nRow >= 0 and nRow < N and nCol >= 0 and nCol < N and (nRow,nCol) not in visited:
                    heapq.heappush(heap, (-grid[nRow][nCol], nRow,nCol))
                    visited.add((nRow,nCol))
                
            
            
            
                       
                       
        
        