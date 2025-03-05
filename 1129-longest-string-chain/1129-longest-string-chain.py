class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        c = {} 
        s = sorted(words, key=len)
        for w in s:
            c[w] = 1 
            for i in range(len(w)):
                p = w[:i] + w[i+1:]
                if p in c:
                    c[w] = max(c[w], c[p] + 1)
        return max(c.values())