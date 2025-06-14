class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        t = s
        pos = 0
        while pos < len(s) and s[pos] == "9":
            pos += 1
        if pos < len(s):
            s = s.replace(s[pos], "9")
        t = t.replace(t[0], "0")
        return int(s) - int(t)