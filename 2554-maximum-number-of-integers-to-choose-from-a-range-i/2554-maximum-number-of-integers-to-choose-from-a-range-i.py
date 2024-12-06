class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ans, banned = -1, set(banned)
        for i in range(1,n+1):
            if i in banned: 
                continue             
            maxSum-= i
            ans += 1
            if maxSum < 0: 
                return ans
        return ans+1