class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        st = []
        for i in strs:
            if i.isdigit():
                st.append(int(i))
                # print(i)
            else:
                st.append(len(i))
        return max(st)