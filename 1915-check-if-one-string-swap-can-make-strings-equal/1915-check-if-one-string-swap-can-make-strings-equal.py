class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        diff = [(a, b) for a, b in zip(s1, s2) if a != b]
        return len(diff) == 2 and diff[0] == diff[1][::-1]