class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        v = {'a','e','i','o','u'}
        c=0
        for i in range(left,right+1):
            w=words[i]
            if w[0] in v and w[-1] in v:
                c+=1
        return c