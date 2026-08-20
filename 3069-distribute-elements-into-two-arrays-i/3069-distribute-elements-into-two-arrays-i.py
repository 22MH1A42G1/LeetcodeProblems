class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n<2: return nums
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        res = []
        for i in range(2,n):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        print(arr1,arr2)
        res = arr1+arr2
        return res