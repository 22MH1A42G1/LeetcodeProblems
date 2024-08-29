class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        count = 1
        for i in nums:
            if(i<count):
                continue
            elif(count!=i):
                return count
            else:
                count+=1
        return count