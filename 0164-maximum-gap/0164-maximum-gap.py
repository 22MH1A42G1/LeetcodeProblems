class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        c = 0
        nums.sort()
        for i in range(len(nums)-1):
            n = nums[i+1] - nums[i]
            c = max(c, n)
        return c