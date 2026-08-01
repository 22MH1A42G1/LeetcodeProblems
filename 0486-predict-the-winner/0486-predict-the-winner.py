class Solution:
    def score(self, nums: List[int],i: int,j: int) -> int:
        if i==j:
            return nums[i]
        l = nums[i]-self.score(nums,i+1,j) 
        r = nums[j]-self.score(nums,i,j-1) 
        return max(l,r)

    def predictTheWinner(self, nums: List[int]) -> bool:
        return self.score(nums,0,len(nums)-1)>= 0