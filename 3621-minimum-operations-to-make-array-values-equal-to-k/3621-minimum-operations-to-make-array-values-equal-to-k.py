class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        st = set(x for x in nums if x>k)
        for x in nums:
            if x<k:
                return -1
        return len(st)