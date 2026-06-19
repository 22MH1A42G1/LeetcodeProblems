class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        g = 0
        m = 0
        for i in gain:
            g+=i
            m = max(m,g)
        return m