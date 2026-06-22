class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter
        textCount = Counter(text)
        minCount = min(
            textCount['b'],
            textCount['a'],
            textCount['l']//2,
            textCount['o']//2,
            textCount['n']
        )
        return minCount