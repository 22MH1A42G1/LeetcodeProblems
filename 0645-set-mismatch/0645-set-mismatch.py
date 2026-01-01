class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = (1 + len(nums))*len(nums) // 2
        cs = sum(nums)
        ms = sum(set(nums))
        mn = s - ms
        dn = cs - ms
        return [dn, mn]
