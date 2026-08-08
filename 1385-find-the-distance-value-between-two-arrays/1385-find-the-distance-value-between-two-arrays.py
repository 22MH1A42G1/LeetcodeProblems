class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        c = 0
        for i in arr1:
            for j in arr2:
                if abs(i-j) <= d:
                    c+=1
                    break
        return len(arr1)- c
