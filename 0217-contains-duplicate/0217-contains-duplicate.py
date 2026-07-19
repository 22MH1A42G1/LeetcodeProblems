class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ls = len(set(nums)) 
        l = len(nums)
        # print(ls==l)
        return not ls==l