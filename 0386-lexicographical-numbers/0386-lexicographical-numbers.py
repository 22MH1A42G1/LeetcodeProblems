class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def fun(i,n,arr):
            if i>n: return
            arr.append(i)
            for j in range(10):
                nn = i*10+j
                if nn<=n: fun(nn,n,arr)
                else: break
        arr = []
        for i in range(1,10):
            fun(i,n,arr)
        return arr