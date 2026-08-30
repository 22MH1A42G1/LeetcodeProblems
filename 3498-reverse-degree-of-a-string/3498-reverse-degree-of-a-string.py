from collections import defaultdict
class Solution:
    def reverseDegree(self, s: str) -> int:
        ira = list(range(26,0,-1))
        l = [chr(i) for i in range(97,123)]
        # print((l,ira))
        f = defaultdict(int)
        for i in range(26):
            f[l[i]]+=f.get(0,ira[i])
        # print(f)
        ans = 0
        for i in range(len(s)):
            ans += (f[s[i]]*(i+1))
        return ans