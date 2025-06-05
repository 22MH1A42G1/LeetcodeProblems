class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[] # list as a stack
        for i in tokens:
            #checking the current token is a symbol
            if i in "+/*-":
                op2 = st.pop()
                op1 = st.pop()
                if i=="+":
                    st.append(op1+op2)
                elif i=="-":
                    st.append(op1-op2)
                elif i=="*":
                    st.append(op1*op2)
                else:
                    st.append(int(op1/op2))
            else:
                st.append(int(i))
        return st[-1]