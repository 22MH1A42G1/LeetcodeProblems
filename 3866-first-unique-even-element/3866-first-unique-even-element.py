class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        ans = -1
        for i in nums:
            if i%2==0 and nums.count(i)==1:
                ans = i
                break
        return ans