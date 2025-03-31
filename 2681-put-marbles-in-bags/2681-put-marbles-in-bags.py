class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        l = []
        for i in range(n-1):
            l.append(weights[i]+weights[i+1])
        l.sort()
        a = 0
        for i in range(k-1):
            a += l[n-2-i]-l[i]
        return a