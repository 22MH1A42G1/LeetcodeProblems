class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        r, p = [1], 1
        for k in range(1, rowIndex+1):
            n = p*(rowIndex-k+1)//k
            r.append(n)
            p = n
        return r