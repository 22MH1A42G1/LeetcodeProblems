class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        x = [0]*n
        y = [0]*m
        c = 0
        for i,j in indices:
            y[i]+=1
            x[j]+=1
        # print(y,x)
        for k in y:
            for l in x:
                c += (k+l)%2
        return c