class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        l = []
        c = 0
        for i in grid:
            for j in i:
                l.append(j)
        for i in l:
            if i<0:
                c+=1
        return c