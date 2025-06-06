class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        f = [j for i in grid for j in i]
        c = Counter(f)
        for i in range(1, n*n+1):
            if c[i] == 2: repeated = i
            if c[i] == 0: missing = i
        return [repeated, missing]