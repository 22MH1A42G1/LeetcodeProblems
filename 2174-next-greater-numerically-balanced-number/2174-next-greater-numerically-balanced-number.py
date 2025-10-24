class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        for i in range(n+1, 1224445):
            c = Counter(str(i))
            if all(c[d]==int(d) for d in c):
                return i