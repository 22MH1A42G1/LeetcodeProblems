class Solution:
    def smallestPalindrome(self, s: str) -> str:
        f=sorted(s[:len(s)//2])
        m=[]
        if len(s)%2==1:
            m.append(s[len(s)//2])
        res=f+m+f[::-1]
        return ''.join(map(str,res))