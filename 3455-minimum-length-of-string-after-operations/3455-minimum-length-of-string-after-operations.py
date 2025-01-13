class Solution:
    def minimumLength(self, s: str) -> int:
        #return sum(1 if x % 2 else 2 for x in Counter(s).values())
        c=0
        cs=Counter(s)
        for i in cs.values():
            if i%2:
                c+=1
            else:
                c+=2
        return c