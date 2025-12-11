class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        xMax, yMax=[0]*(n+1), [0]*(n+1)
        xMin, yMin=[1<<31]*(n+1), [1<<31]*(n+1)

        for x, y in buildings:
            xMin[y]=min(xMin[y], x)
            xMax[y]=max(xMax[y], x)
            yMin[x]=min(yMin[x], y)
            yMax[x]=max(yMax[x], y)

        cnt=0
        for x, y in buildings:
            coverX=(xMin[y]<x & x<xMax[y])
            coverY=(yMin[x]<y & y<yMax[x])
            cnt+=(coverX & coverY)
        return cnt