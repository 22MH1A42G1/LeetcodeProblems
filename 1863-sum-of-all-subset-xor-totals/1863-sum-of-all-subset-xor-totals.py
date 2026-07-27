class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        s=0
        x=0
        n=len(nums)-1
        for i in nums: 
            x|=i
            s+=x
        return (x)*(1<<n)