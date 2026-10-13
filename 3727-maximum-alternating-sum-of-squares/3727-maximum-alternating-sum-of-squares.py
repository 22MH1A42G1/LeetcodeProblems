class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        l = [i*i for i in nums]
        l.sort()
        m = len(l)//2
        l1 = l[:m]
        l2 = l[m:]
        print(l1,l2)
        return abs(sum(l2)-sum(l1))