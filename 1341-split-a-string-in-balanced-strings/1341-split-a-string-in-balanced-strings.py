class Solution:
    def balancedStringSplit(self, s: str) -> int:
        st=[]
        c=0
        for i in s:
            if not st or st[-1]==i: st.append(i)
            else:
                st.pop()
                if not st: c+=1
        return c