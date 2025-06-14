class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        n=''
        for i in words:
            t=str(i)
            n+=t[0]
        return n==s