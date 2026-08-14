class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element=None
        count=0
        for n in nums:
            if count==0:
                element=n
            count+=(1 if n==element else -1)
        return element