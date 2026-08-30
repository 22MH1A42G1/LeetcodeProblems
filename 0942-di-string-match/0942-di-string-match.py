class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        l, h = 0, len(s)
        ans = []
        for i in s:
            if i == "I":
                ans.append(l)
                l += 1
            else:
                ans.append(h)
                h-=1
        return ans + [l]