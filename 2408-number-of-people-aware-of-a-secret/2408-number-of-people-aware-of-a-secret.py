class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        share, MOD = 0, 10**9 + 7
        for t in range(2, n + 1):
            if t - delay > 0:
                share = (share + dp[t - delay] + MOD) % MOD
            if t - forget > 0:
                share = (share - dp[t - forget] + MOD) % MOD
            dp[t] = share
        know = 0
        for i in range(n - forget + 1, n + 1):
            know = (know + dp[i]) % MOD
        return know