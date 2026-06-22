class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        from collections import Counter
        targetCounter = Counter(target)
        stringCounter = Counter(s)
        rearrangeMinCounter = float('inf')
        for i,j in targetCounter.items():
            if i not in stringCounter.keys():
                return 0
            rearrangeMinCounter = min(
                stringCounter[i]//j,
                rearrangeMinCounter
            )
        return rearrangeMinCounter