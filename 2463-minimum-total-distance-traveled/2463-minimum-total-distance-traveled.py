class Solution:
    def minimumTotalDistance(self, A: List[int], B: List[List[int]]) -> int:
        A.sort()
        B.sort()
        @lru_cache(None)
        def dp(i, j, k):
            if i == len(A): return 0
            if j == len(B): return inf
            res1 = dp(i, j + 1, 0)
            res2 = dp(i + 1, j, k + 1) + abs(A[i] - B[j][0]) if B[j][1] > k else inf
            return min(res1, res2)
        return dp(0, 0, 0)