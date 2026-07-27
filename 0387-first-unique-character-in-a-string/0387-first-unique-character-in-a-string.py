class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        for i,j in c.items():
            if j==1:
                return s.index(i)
        return -1