class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        if len(target) > 0:
            j = 0
            for i in range(1, target[-1] + 1):
                ans.append("Push")
                if i != target[j]:
                    ans.append("Pop")
                else:
                    j += 1
        return ans