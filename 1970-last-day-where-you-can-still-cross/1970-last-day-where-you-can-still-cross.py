class Solution:
    def latestDayToCross(self, r: int, c: int, a: List[List[int]]) -> int:
        def check(k):
            def dfs(i,j,g={*map(tuple,a[:k+1])}):
                if not (0<i<=r and 0<j<=c) or (i,j) in g: return 1 # stuck
                if i==r: return 0 # pass
                g.add((i,j))
                return all(starmap(dfs,((i,j+1),(i+1,j),(i-1,j),(i,j-1))))
            
            return all(dfs(1,j+1) for j in range(c))

        return bisect_left(range(len(a)),1,key=check)