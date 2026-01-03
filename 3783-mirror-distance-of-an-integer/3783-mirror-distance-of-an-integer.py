class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev = "".join(reversed(str(n)))
        return abs(int(rev)-n)