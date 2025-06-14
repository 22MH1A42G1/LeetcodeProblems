class Solution:
    def scoreOfString(self, s: str) -> int:
        i, j = 0, 1
        ans = 0
        while i<len(s)-1 and j<len(s):
            a = ord(s[i])
            b = ord(s[j])
            ans += abs(a - b)
            i += 1
            j += 1
        return ans