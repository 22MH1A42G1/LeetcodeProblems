class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = []
        def dfs(curr):
            if len(ans) == k:
                return
            if len(curr) == n:
                ans.append(curr)
                return
            for x in ['a', 'b', 'c']:
                if not curr or curr[-1] != x:
                    dfs(curr + x)
        dfs("")
        return ans[k-1] if len(ans) >= k else ''