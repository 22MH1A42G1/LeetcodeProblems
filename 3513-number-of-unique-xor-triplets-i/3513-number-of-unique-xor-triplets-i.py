class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        return len(nums) if len(nums) < 3 else 2**ceil(log2(len(nums)+1))