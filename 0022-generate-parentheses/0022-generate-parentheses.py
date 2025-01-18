class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(a,b,s):
            if a==b and a+b==n*2:
                res.append(s)
                return
            if a<n:
                dfs(a+1,b,s+"(")
            if b<a:
                dfs(a,b+1,s+")")
        dfs(0,0,"")
        return res