class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        st=[]
        for i in range(left,right+1):
            temp, d = i, True
            while temp>0:
                r = temp%10
                if r==0 or i%r!=0:
                    d=False
                    break
                temp//=10
            if d: st.append(i)
        return st