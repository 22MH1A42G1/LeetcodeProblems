class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        l = len(words[0])
        tl = len(target)
        mod = 1000000007
        cf = [[0] * 26 for _ in range(l)]
        for word in words:
            for j in range(l):
                cf[j][ord(word[j]) - ord("a")] += 1
        dp = [[0] * (tl + 1) for _ in range(l + 1)]
        for curr_word in range(l + 1):
            dp[curr_word][0] = 1
        for curr_word in range(1, l + 1):
            for curr_target in range(1, tl + 1):
                dp[curr_word][curr_target] = dp[curr_word - 1][curr_target]
                cur_pos = ord(target[curr_target - 1]) - ord("a")
                dp[curr_word][curr_target] += (
                    cf[curr_word - 1][cur_pos]
                    * dp[curr_word - 1][curr_target - 1]
                ) % mod
                dp[curr_word][curr_target] %= mod
        return dp[l][tl]