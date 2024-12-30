class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return []
        if numRows == 1: return [[1]]
        p = self.generate(numRows-1)
        n = [1]*numRows
        for i in range(1, numRows-1):
            n[i] = p[-1][i-1] + p[-1][i]
        p.append(n)
        return p