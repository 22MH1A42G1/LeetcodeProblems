class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mi = inf
        res = 0
        for i in nums:
            mi = min(mi, i)
            res = max(res, i - mi)
        return -1 if res == 0 else res