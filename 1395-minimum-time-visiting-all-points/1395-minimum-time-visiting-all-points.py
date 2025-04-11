class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        c = 0
        for i in range(len(points)-1):
            x,y=points[i]
            a,b=points[i+1]
            c+=max(abs(a-x),abs(b-y))
        return c