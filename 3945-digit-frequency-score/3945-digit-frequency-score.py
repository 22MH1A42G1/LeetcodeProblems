class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        from collections import Counter
        d = [int(i) for i in str(n)]
        freq = Counter(d)
        ans = 0
        for i,j in freq.items():
            ans+=(i*j)
        return ans