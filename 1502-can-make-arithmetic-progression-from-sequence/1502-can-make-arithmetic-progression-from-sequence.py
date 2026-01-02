class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        d = abs(arr[1] - arr[0])
        for i in range(2, len(arr)):
            if abs(arr[i] - arr[i-1]) != d:
                return False
        return True