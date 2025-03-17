class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        s = set()
        for i in nums:
            if i in s:
                s.remove(i)
            else:
                s.add(i)
        return not s