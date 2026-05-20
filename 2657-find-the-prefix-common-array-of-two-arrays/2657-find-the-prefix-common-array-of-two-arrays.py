class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        C = []
        for i in range(n):
            c1 = set(A[:i+1])
            c2 = set(B[:i+1])
            C.append(len(c1.intersection(c2)))
        return C
