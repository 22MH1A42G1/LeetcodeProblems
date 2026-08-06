class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c = Counter(t)
        for i in s:
            c[i]-=1
            if c[i]==0:
                del c[i]
        return list(c.keys())[0]