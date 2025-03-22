class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        s, z = ''.join(map(chr,range(n))), Counter()
        for v,u in sorted(map(sorted,edges)): # small elements go first
            s = s.replace(s[u],s[v]) # union
            z[s[v]] += 1 # counting edges in component
                         # s[v] - root of union - smallest element
        return sum(z[c]==comb(f,2) for c,f in Counter(s).items())
        # comb(f,2) == f*(f-1)//2