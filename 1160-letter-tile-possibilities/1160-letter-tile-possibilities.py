class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        s = set()
        for i in range(1,len(tiles)+1):
            for p in permutations(tiles,i):
                s.add(p)
        l = len(s)
        return l
        # from collections import Counter
        # c = Counter(tiles)
        # def fun(c,tiles):
        #     t=0
        #     for i,k in c.items():
        #         tiles+=i
        #         c[i]-=k
        #         t=fun(t,c)
        #         c[i]+=t

        # return fun(c,tiles)
