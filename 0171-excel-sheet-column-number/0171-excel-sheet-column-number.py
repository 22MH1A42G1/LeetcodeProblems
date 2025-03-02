class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        t=0
        for i in columnTitle:
            a=ord(i)-64
            t*=26
            t+=a
        return t