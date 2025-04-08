class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c=0
        while len(nums)>len(set(nums)):
            nums=nums[3:]
            c+=1
        return c