class Solution:
    def arrangeCoins(self, n: int) -> int:
        k = 0
        while k * (k + 1) // 2 <= n:
            k += 1
        return k - 1