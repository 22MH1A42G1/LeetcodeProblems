class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        d = [(0,1),(0,-1),(1,0),(-1,0)]
        
        def dfs(grid,r,c,mc,cost,q):
            def fun(mc,r,c):
                return 0<=r<len(mc) and 0<=c<len(mc[0]) and mc[r][c]==float("inf")

            if not fun(mc,r,c):
                return
            mc[r][c]=cost
            q.append((r,c))
            nd=grid[r][c]-1
            dx,dy= d[nd]
            dfs(grid,r+dx,c+dy,mc,cost,q)

        r,c = len(grid), len(grid[0])
        cost = 0
        mc = [[float("inf")]*c for _ in range(r)]
        q = deque()
        dfs(grid, 0, 0, mc,cost, q)
        while q:
            cost +=1
            ls = len(q)
            for _ in range(ls):
                row, col = q.popleft()
                for di,(dx,dy) in enumerate(d):
                    dfs(grid,row+dx,col+dy,mc,cost,q)
        return mc[r-1][c-1]