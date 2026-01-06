class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l=[]
        for a, b in zip_longest(word1, word2, fillvalue=''):
            l.append(a+b)
        return "".join(l)