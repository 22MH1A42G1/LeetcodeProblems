class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        dp = [0]
        for i in range(len(derived)):
            dp.append(derived[i]^dp[i])
        z=(dp[0]==dp[-1])
        dp = [1]
        for i in range(len(derived)):
            dp.append(derived[i]^dp[i])
        o=(dp[0]==dp[-1])
        return z or o