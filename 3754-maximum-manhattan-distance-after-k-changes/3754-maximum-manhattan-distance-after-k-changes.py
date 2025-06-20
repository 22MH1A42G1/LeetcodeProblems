class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ans = 0
        north = south = east = west = 0
        for it in s:
            if it == "N":
                north += 1
            elif it == "S":
                south += 1
            elif it == "E":
                east += 1
            elif it == "W":
                west += 1
            times1 = min(north, south, k)  # modification times for N and S
            times2 = min(
                east, west, k - times1
            )  # modification times for E and W
            ans = max(
                ans,
                self.count(north, south, times1)
                + self.count(east, west, times2),
            )
        return ans

    def count(self, drt1: int, drt2: int, times: int) -> int:
        return (
            abs(drt1 - drt2) + times * 2
        )  # Calculate modified Manhattan distance