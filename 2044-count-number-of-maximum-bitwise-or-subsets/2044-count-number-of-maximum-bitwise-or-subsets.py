import collections
from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def h(A):
            dp = Counter([0]) 
            for a in A:
                for k, v in list(dp.items()): 
                    dp[k | a] += v 
            return dp[max(dp)] 
        
        return h(nums)
