class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ws = sum(nums[:k])
        ms = ws
        for i in range(k, len(nums)):
            ws=ws-nums[i-k]+nums[i]
            ms=max(ms,ws)
        return ms/k