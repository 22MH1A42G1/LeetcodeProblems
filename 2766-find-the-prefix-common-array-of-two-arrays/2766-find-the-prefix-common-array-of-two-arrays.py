class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n =len(A)
        pc =[0]*n
        for i in range(n):
            c=0
            for j in range(i+1):
                for k in range(i+1):
                    if A[j] == B[k]:
                        c += 1
                        break
            pc[i] = c
        return pc