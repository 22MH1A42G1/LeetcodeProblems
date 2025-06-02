class Solution:
    def removeDuplicates(self, s: str) -> str:
        m = []
        for i in s:
            if m and m[-1]==i:
                m.pop()
            else:
                m.append(i)
        return "".join(m)
                