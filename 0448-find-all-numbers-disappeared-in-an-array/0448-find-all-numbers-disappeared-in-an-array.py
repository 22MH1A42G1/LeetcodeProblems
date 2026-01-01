class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        n = len(nums)
        ans = []
        for i in range(1,n+1):
            if i not in s:
                ans.append(i)
        return ans