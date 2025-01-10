from collections import Counter
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        req = Counter()
        for word in words2:
            cur = Counter(word)
            for ch in cur:
                req[ch] = max(req[ch], cur[ch])
        ans = []
        for word in words1:
            cur = Counter(word)
            if all(cur[ch] >= req[ch] for ch in req):
                ans.append(word)
        return ans   