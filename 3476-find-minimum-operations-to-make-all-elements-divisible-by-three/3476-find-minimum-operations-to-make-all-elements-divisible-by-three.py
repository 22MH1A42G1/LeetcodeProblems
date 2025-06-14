class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c = sum(1 for i in nums if i%3==0)
        return len(nums) - c