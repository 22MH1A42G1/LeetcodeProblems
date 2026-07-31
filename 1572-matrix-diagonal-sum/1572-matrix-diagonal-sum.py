class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        c = 0
        for i in range(len(mat)): # 0 1 2 3
            for j in range(len(mat[0])): # 0 1 2 3
                if i==j or j==len(mat)-1-i: #
                    c+=mat[i][j]
        return c