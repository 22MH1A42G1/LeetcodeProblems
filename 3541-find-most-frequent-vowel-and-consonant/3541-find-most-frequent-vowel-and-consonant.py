class Solution:
    def maxFreqSum(self, s: str) -> int:
        v = 'aeiou'
        d = Counter(s)
        vl = max((d[i] for i in d if i in v), default=0)
        c = max((d[i] for i in d if i not in v), default=0)
        return vl + c