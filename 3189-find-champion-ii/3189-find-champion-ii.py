class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        i = [True]*n
        for w,l in edges:
            i[l] = False
        c, s = -1, 0
        for t in range(n):
            if i[t]:
                c=t
                s+=1
        if s == 1:
            return c
        return -1
