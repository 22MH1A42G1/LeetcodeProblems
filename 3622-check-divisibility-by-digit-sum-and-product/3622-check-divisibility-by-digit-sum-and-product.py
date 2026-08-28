class Solution:
    def checkDivisibility(self, n: int) -> bool:
        nums = [int(i) for i in str(n)]
        s = sum(nums)
        p = 1
        for i in nums:
            p*=i
        
        return n %(s+p) == 0