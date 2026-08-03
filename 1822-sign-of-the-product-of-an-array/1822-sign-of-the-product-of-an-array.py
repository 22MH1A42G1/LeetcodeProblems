class Solution:
    def arraySign(self, nums: List[int]) -> int:
        p = 1
        for i in nums:
            p*=i
        return 1 if p > 0 else 0 if p==0 else -1