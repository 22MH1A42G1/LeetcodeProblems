class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        v = sorted([i for r in grid for i in r])
        df = [abs(i - v[0]) % x for i in v]
        if any(d != 0 for d in df):
            return -1
        m = v[len(v) // 2]
        o = sum(abs(i - m) // x for i in v)
        return o
        