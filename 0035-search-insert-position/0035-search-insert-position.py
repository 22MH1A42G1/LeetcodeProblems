class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        for i, num in enumerate(nums):
            if num >= target:
                return i
        return len(nums)