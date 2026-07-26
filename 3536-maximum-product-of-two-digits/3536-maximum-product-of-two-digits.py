class Solution:
    def maxProduct(self, n: int) -> int:
        l = [int(i) for i in str(n)]
        l.sort()
        return l[-1]*l[-2]