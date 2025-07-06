class FindSumPairs:

    def __init__(self, nums1: list[int], nums2: list[int]):
        self.n1 = nums1
        self.n2 = nums2
        self.m = Counter(nums2)

    def add(self, i: int, v: int) -> None:
        old_val = self.n2[i]
        self.m[old_val] -= 1
        self.n2[i] += v
        self.m[self.n2[i]] += 1

    def count(self, t: int) -> int:
        c = 0
        for x in self.n1:
            c += self.m[t - x]
        return c