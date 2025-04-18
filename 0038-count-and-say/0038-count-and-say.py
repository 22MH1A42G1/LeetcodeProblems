class Solution:
    def countAndSay(self, n: int) -> str:
        r="1"
        for _ in range(n-1):
            t,i="",0
            while i< len(r):
                c=1
                while i+1<len(r) and r[i]==r[i+1]:
                    i+=1
                    c+=1
                t+=str(c)+r[i]
                i+=1
            r=t
        return r