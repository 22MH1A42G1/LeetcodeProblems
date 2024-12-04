class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        j, n, m = 0, len(str1), len(str2)
        for i in range(n):
            if j < m and (ord(str2[j]) - ord(str1[i])) % 26 <= 1:
                j += 1
        return j == m