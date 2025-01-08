class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        c=0
        n=len(words)
        for i in range(n):
            for j in range(i+1,n):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    c+=1
        return c