import numpy as np
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        i = np.argsort(arr)
        m = np.vectorize(lambda x: i[x-1])(mat)
        return int(min(m.max(axis=0).min(),m.max(axis=1).min()))