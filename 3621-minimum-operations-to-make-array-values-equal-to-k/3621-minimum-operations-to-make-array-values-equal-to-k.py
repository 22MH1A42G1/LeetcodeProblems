class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        if min(nums) < k:
            return -1
        return len(set(nums)) + (min(nums) > k) - 1