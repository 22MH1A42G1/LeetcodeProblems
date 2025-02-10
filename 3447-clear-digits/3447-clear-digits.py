class Solution:
    def clearDigits(self, s: str) -> str:
        st = ""
        for i in s:
            if not i.isdigit():
                st = st + i
            else:
                st = st[:len(st)-1]
        return st