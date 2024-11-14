class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l, h = 1, max(quantities)
        while l < h: 
            m = l + h >> 1
            if sum(ceil(i/m) for i in quantities) <= n: h = m 
            else: l = m + 1
        return l