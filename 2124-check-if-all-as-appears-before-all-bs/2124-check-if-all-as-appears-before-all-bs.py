class Solution:
    def checkString(self, s: str) -> bool:
        t = ''.join(map(str,sorted(s)))
        return s==t