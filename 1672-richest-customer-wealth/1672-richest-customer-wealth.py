class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ms = 0
        for i in accounts:
            cs = 0
            for j in i:
                cs += j
            ms = max(cs, ms)
        return ms