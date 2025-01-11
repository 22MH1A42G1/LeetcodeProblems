from collections import Counter
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        c = Counter(s)
        o = sum(i % 2 for i in c.values())
        return o <= k