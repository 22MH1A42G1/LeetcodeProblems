class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c = 0 
        for i in words:
            if all(j in allowed for j in i):
                c+=1
            else:
                continue
        return c