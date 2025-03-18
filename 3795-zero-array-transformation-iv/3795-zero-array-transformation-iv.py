class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        s = [{0} for _ in range(len(nums))]
        for k, (l, r, v) in enumerate(queries):
            if all(x in st for x, st in zip(nums, s)):
                return k
            for i in range(l, r + 1):
                l = []
                for x in s[i]:
                    l.append(x + v)
                s[i].update(l)
        return len(queries) if all(x in st for x, st in zip(nums, s)) else -1