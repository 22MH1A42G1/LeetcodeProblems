class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        cw = {}
        wc = {}
        l = s.split(" ")
        if len(pattern)!=len(l):
            return False
        
        return len(set(pattern)) == len(set(l)) == len(set(zip(pattern, l)))
