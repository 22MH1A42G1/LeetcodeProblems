class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        chars = ["a", "b", "c"]
        self.count = 0
        self.result = ""
        def dfs(curr):
            if len(curr) == n:
                self.count += 1
                if self.count == k:
                    self.result = curr
                return
            for ch in chars:
                if not curr or curr[-1] != ch:
                    dfs(curr + ch)
                if self.result: 
                    return
        dfs("")
        return self.result