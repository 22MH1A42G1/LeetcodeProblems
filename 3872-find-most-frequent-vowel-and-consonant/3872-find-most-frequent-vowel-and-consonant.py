class Solution:
    def maxFreqSum(self, s: str) -> int:

        vowels = 'aeiou'
        d = defaultdict(int)

        for ch in s: d[ch]+= 1
        
        mxVow = max((d[ch] for ch in vowels), default = 0)
        for ch in vowels: d[ch] = 0

        mxCon = max(d.values())
        return mxVow + mxCon