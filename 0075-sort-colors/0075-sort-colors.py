class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a,b,c=0,0,0
        for i in nums:
            if i==0:
                a+=1
            if i==1:
                b+=1
            if i==2:
                c+=1
        nums[:a] = [0] * a
        nums[a:a+b] = [1] * b
        nums[a+b:] = [2] * c