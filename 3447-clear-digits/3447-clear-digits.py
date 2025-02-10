class Solution:
    def clearDigits(self, s: str) -> str:
        l=[]
        for i in s:
            if i.isdigit() and l:
                l.pop()
            else:
                l.append(i)
        return "".join(l)