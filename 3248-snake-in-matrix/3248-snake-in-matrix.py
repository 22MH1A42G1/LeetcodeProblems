class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        dp = {"LEFT":-1,"RIGHT":1,"UP":-n,"DOWN":n}
        c = 0
        for i in commands:
            c += dp[i]
        return c