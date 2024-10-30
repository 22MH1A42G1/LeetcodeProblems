class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        dp1, dp2 = [1]*n, [1]*n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]: dp1[i] = max(dp1[i], 1+dp1[j])
                if nums[j] > nums[i]: 
                    if dp1[j] > 1: dp2[i] = max(dp2[i], 1 + dp1[j])
                    if dp2[j] > 1: dp2[i] = max(dp2[i], 1 + dp2[j])
        
        return n - max(dp2)