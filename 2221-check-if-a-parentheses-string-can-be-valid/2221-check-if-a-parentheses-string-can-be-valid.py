class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n=len(s)
        if n&1==1: return False
        bMin, bMax=0, 0 
        for i, c in enumerate(s):
            op=c== '('
            wild=locked[i]=='0'
            if (not op) or wild: bMin-=1  
            else: bMin+=1  
            if op or wild: bMax+=1  
            else: bMax-=1  
            if bMax < 0: return False
            bMin = max(bMin, 0)
        return bMin==0