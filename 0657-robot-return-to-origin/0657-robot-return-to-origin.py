class Solution:
    def judgeCircle(self, moves: str) -> bool:
        u = moves.count("U")
        d = moves.count("D")
        l = moves.count("L")
        r = moves.count("R")
        return u == d and l==r