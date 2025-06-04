class Solution:
    def resultingString(self, s: str) -> str:
        st=[]
        for i in s:
            if st:
                t=st[-1]
                d=abs(ord(t)-ord(i))
                if d==1 or d==25:
                    st.pop()
                    continue
            st.append(i)
        return "".join(st)