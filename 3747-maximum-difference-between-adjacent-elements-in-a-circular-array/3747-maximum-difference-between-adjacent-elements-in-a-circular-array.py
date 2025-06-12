class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        return max(abs(nums[i-1] - nums[i]) for i in range(len(nums)))