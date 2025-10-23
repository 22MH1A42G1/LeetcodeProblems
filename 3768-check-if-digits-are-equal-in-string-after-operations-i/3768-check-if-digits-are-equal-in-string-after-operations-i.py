class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s)!=2:
            temp=[]
            for i in range(1,len(s)):
                temp.append(str((int(s[i-1])+int(s[i]))%10))
            s="".join(temp)
        return s[0]==s[1]