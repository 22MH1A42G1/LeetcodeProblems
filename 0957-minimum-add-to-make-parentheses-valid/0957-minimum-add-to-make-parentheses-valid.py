class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        o,c=0,0
        for i in s:
            if i == '(': o+=1
            elif i == ')' and o>0: o-=1
            else: c+=1
        return o+c