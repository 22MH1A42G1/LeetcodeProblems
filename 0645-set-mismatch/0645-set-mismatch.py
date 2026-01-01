class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = list(range(1,len(nums)+1))
        l = list(set(nums))
        ans = []
        # duplicate
        mp = Counter(nums)
        for i,j in mp.items():
            if j>1:
                ans.append(i)
        # missing 
        for i in s:
            if i not in nums:
                ans.append(i)
        return ans
