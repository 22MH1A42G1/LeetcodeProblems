class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c, w = Counter(s1), len(s1)
        for i in range(len(s2)):
            if s2[i] in c:
                c[s2[i]]-=1
            if i >= w and s2[i-w] in c: 
                c[s2[i-w]]+=1
            if all([c[i]==0 for i in c]):
                return True
        return False