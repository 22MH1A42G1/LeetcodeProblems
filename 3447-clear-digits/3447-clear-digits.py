class Solution:
    def clearDigits(self, s: str) -> str:
        l=[]
        for i in s:
            if(i.isalpha()):
                l.append(i)
            else:
                l.pop()
        return "".join(l)