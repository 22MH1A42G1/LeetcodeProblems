class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = []
        for i in nums:
            ans.append(sum(int(j) for j in str(i)))
        return min(ans)