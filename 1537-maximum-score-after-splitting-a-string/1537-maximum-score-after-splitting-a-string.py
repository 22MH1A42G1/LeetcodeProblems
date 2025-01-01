class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0
        for i in range(0,len(s)-1):
            c = 0
            for j in range(0,i+1):
                if s[j]=='0': 
                    c+=1
            for j in range(i+1,len(s)):
                if s[j]=='1': 
                    c+=1
            ans = max(ans,c)
        return ans