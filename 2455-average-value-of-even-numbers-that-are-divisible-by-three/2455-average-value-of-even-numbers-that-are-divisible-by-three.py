class Solution:
    def averageValue(self, nums: List[int]) -> int:
        s=0
        c=0
        for i in nums:
            if i%2==0 and i%3==0:
                c+=i
                s+=1
        return c//s  if s >0 else 0