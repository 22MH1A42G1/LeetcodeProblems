class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def f(n,k):
            m = floor((2**(n-1) + 0.5))
            if n == 1 and k == 1:
                return 0
            elif n != 1 and k == m:
                return 1
            elif k < m:
                return f(n-1,k)
            elif k > m:
                return not f(n,m - abs(m-k))
        return str(int(f(n,k)))
        