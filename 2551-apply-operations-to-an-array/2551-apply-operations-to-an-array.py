class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = []
        for i in range(n-1):
            if nums[i]==nums[i+1] and nums[i]!=0:
                nums[i]*=2
                nums[i+1]=0
        for i in nums:
            if i != 0:
                l.append(i)
        while len(l) < n:
            l.append(0)
        return l