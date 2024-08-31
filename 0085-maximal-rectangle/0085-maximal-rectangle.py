class Solution:
    def maximalRectangle(self, M: List[List[str]]) -> int:
        m, n ,a= len(M), len(M[0]),0
        dp = [0]*(n+1)
        for i in range(m):
            s = deque([-1])
            for j in range(n+1):
             if j<n and M[i][j]=='1': 
                    dp[j]+= 1
             else: dp[j] = 0
             while(dp[s[0]] > dp[j]):
              a=max(a,dp[s.popleft()]*(j-s[0]-1))
             s.appendleft(j)
        return a