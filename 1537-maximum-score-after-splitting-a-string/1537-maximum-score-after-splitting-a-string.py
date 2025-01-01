class Solution:
    def maxScore(self, s: str) -> int:
        ##Brute Force
        # ans = 0
        # for i in range(0,len(s)-1):
        #     c = 0
        #     for j in range(0,i+1):
        #         if s[j]=='0': 
        #             c+=1
        #     for j in range(i+1,len(s)):
        #         if s[j]=='1': 
        #             c+=1
        #     ans = max(ans,c)
        # return ans

        ##Count Left 0's & Right 1's
        # o,z,a=s.count("1"),0,0
        # for i in range(len(s)-1):
        #     if s[i] == "1": 
        #         o-=1
        #     else: 
        #         z+=1
        #     a = max(a,z+o)
        # return a

        ##1 pass
        # o,z,m=0,0,float("-inf")
        # for i in range(len(s)-1):
        #     if s[i]=="1":
        #         o+=1
        #     else:
        #         z+=1
        #     m = max(m,z-o)
        # if s[-1]=="1":
        #     o+=1
        # return m+o

        o = s.count('1')
        mx = 0
        for i in s[:-1]:
            o += (i=="0")-(i=="1")
            mx = max(mx,o)
        return mx