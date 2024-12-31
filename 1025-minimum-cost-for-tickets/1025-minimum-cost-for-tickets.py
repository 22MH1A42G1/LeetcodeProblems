class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [0] * (n + 1)
        for i in range(n):
            j = bisect_right(days, days[i] - 7)
            k = bisect_right(days, days[i] - 30)
            dp[i + 1] = min(dp[i] + costs[0], dp[j] + costs[1], dp[k] + costs[2])
        return dp[-1]