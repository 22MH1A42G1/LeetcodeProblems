class Solution:
    # def roman(self, s: str) -> int:
    #     match(s):
    #         case 'I': return -1 if s[1]=='V' or s[1]=='X' else 1
    #         case 'V': return 5 
    #         case 'X': return -10 if s[1]=='L' or s[1]=='C' else 10
    #         case 'L': return 50
    #         case 'C': return -100 if s[1]=='D' or s[1]=='M' else 100
    #         case 'D': return 500
    #         case 'M': return 1000
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'V':5, 'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,"CM":900}
        ans = 0
        i =0
        while i < len(s):
            if s[i:i+2] in d:
                ans+=d[s[i:i+2]]
                i+=2
            else:
                ans+=d[s[i]]
                i+=1
        return ans


        # for i in range(len(s)-1):
        #     if s[i]=='I':
        #         if s[i+1]=='V':
        #             ans+=4
        #         elif s[i+1]=='X':
        #             ans+=9
        #         else:
        #             ans+=1
        #     elif s[i]=='X':
        #         if s[i+1]=='L':
        #             ans+=40
        #         elif s[i+1]=='C':
        #             ans+=90
        #         else:
        #             ans+=10
        #     elif s[i]=='C':
        #         if s[i+1]=='D':
        #             ans+=400
        #         elif s[i+1]=='M':
        #             ans+=900
        #         else:
        #             ans+=10
            
        # return ans
