class Solution:
    def rotatedDigits(self, n: int) -> int:
        return sum(
            any(c in '2569' for c in s) and not any(c in '347' for c in s)
            for s in map(str, range(1, n+1))
        )