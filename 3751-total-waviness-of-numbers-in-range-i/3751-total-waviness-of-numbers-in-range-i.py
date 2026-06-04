class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def w(n):
            s = str(n)
            if len(s)<3: return 0
            w = 0
            for i in range(1,len(s)-1):
                l=s[i-1]
                m=s[i]
                r=s[i+1]
                if m>l and m>r: w+=1
                elif m<l and m<r: w+=1
            return w
        res = 0
        for i in range(num1,num2+1):
            res+=w(i)
        return res
