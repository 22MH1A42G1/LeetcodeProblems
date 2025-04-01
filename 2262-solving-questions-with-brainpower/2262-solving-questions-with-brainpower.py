class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        dp[n-1] = questions[n-1][0]
        for i in range(n-2,-1,-1):
            p,b = questions[i]
            a = min(i + b + 1 , n)
            s = p + (dp[a] if a < n else 0)
            sk = dp[i+1]
            dp[i] = max(s , sk)
        return dp[0]