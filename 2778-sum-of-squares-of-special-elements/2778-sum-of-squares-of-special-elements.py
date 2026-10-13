class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        c = 0
        for i in range(len(nums)) :
            if len(nums)%(i+1)==0:
                c += nums[i]**2
        return c