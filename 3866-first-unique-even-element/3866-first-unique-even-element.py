class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        even = Counter(nums)
        ans = -1
        for i,j in even.items():
            if i%2==0 and j==1:
                ans = i
                break
        return ans