class Solution:
    def maximumLength(self, s: str) -> int:
        res = -1
        for c in {*s}:
            q = nlargest(3, findall(c+'+', s)) + ['']*2
            res = max(res, len(q[0])-2, len(q[1])-(q[0]==q[1]), len(q[2]))

        return res or -1