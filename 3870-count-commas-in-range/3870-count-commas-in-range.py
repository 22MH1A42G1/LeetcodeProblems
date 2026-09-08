class Solution:
    def countCommas(self, n: int) -> int:
        return (n>999)*(n-999)