class Solution:
    def coloredCells(self, n: int) -> int:
        c=1
        for i in range(n):
            c += 4*i
        return c