class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            mod = k%n 
            if i%2==0:
                s = mat[i][mod:] + mat[i][:mod]
            else:
                s = mat[i][-mod:]+ mat[i][:-mod]
            if s != mat[i]:
                return False
        return True