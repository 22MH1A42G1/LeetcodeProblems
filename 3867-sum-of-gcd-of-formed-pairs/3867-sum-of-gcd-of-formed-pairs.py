class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        mx = []
        prefixMax = float("-inf")
        for i in nums:
            prefixMax = max(prefixMax, i)
            mx.append(prefixMax)
        prefixGcd = [gcd(i,j) for i,j in zip(nums,mx)]
        prefixGcd.sort()
        ans=0
        l=0
        r=len(nums)-1
        while l < r:
            ans+=gcd(prefixGcd[l],prefixGcd[r])
            l+=1
            r-=1
        return ans
        