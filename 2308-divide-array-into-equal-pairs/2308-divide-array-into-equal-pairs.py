class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        c=Counter(nums)
        for i in c.values():
            if i%2:
                return False
        return True