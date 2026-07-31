class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        missing_array = []
        i = min(nums)  
        while i <= max(nums):
            if i not in nums:
                missing_array.append(i)
            i+=1  
        return missing_array