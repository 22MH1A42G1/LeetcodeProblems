class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        z = s.count('0')
        o = 0
        v = 0
        p = 1

        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                if v + p > k:
                    continue
                v += p
                o += 1
            p <<= 1
            if p > k:
                break
        return z + o