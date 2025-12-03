class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones = 0
        ans=0
        for i in nums:
            if i ==1:
                ones+=1
                ans=max(ans,ones)
            else:
                ones=0
        return ans