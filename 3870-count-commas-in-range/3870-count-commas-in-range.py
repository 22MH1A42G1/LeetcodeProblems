class Solution:
    def countCommas(self, n: int) -> int:
        return sum(1 for i in range(1,n+1) if i>999)