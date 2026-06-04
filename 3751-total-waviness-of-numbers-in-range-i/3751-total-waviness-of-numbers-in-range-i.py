class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        p=(num1,num2)
        def wavi(x):
            s=str(x)
            if len(s)<3: return 0
            w=0
            for i in range(1,len(s)-1):
                l=int(s[i-1])
                m=int(s[i])
                r=int(s[i+1])
                if m>l and m>r: w+=1
                elif m<l and m<r: w+=1
            return w
        t=0
        for n in range(num1,num2+1):
            t+=wavi(n)
        return t