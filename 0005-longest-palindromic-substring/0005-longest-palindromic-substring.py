class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        res = ""
        n = len(s)
        if n==0:
            return 0
        if n==1:
            return s[0]
        if n==2:
            if s==s[::-1]:
                return s
            else:
                return s[0]
        for i in range(n):
            l = i
            r = i
            while l>=0 and r<n and s[l:r+1] == s[l:r+1][::-1]:
                l-=1
                r+=1
            if r-l-1 > len(res):
                res = s[l+ 1:r]
            
            l,r = i, i+1
            while l>=0 and r<n and s[l:r+1] == s[l:r+1][::-1]:
                l-=1
                r+=1
            if r-l-1>len(res):
                res = s[l+1:r]
        return res