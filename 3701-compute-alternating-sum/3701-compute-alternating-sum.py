class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        c=0
        e=[]
        o=[]
        for i in range(len(nums)):
            if i%2==0:
                e.append(nums[i])
            else:
                o.append(nums[i])
        return sum(e)-sum(o)