class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n=len(status)
        canOpen, hasBox=[False]*n, [False]*n
        def dfs(i):
            ans=candies[i]
            for k in keys[i]:
                if not canOpen[k]:
                    canOpen[k]=True
                    if hasBox[k]:
                        ans+=dfs(k)
            for j in containedBoxes[i]:
                hasBox[j]=True
                if canOpen[j]:
                    ans+=dfs(j)
            return ans
        for i in range(n):
            canOpen[i]=status[i]==1
        ans=0
        for i in initialBoxes:
            hasBox[i]=True
            if canOpen[i]:
                ans+=dfs(i)
        return ans
        