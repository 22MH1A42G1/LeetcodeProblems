import numpy as np
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        # i = np.argsort(arr)
        # m = np.vectorize(lambda x: i[x-1])(mat)
        # return int(min(m.max(axis=0).min(),m.max(axis=1).min()))
        m = len(mat)
        n = len(mat[0])
        rows = [n]*m
        cols = [m]*n
        loc = {}
        for i in range(m):
            for j in range(n):
                loc[mat[i][j]] = (i,j)
        for i,val in enumerate(arr):
            row, col = loc[val]
            rows[row]-=1
            cols[col]-=1
            if rows[row]==0 or cols[col]==0:                
                return i