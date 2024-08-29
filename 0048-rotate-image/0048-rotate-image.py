class Solution:
    def rotate(self,m:List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(1, len(m)):
            for j in range(i):
                m[i][j],m[j][i]=m[j][i], m[i][j]
        for i in range(len(m)):
            m[i] = m[i][::-1]