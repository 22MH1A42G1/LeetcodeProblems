class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        d = 0
        f = False
        for i in nums:
            if i == 1:
                if d <= k and f:
                    return False 
                f = True
                d = 0
            d += 1
        return True