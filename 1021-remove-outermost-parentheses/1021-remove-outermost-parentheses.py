class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        st = []
        for i in s:
            if i==")":
                st.pop()
            if st:
                res.append(i)
            if i=="(":
                st.append(i)
        return "".join(res)