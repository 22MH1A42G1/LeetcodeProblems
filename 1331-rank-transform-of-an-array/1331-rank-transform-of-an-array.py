class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s = sorted(set(arr))
        r = {j:i+1 for i,j in enumerate(s)}
        return [r[i] for i in arr]