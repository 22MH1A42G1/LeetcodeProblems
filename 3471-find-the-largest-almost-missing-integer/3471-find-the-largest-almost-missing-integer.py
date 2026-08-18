class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n =  len(nums)
        c = defaultdict(int)
        ans = -1
        for i in range(n-k+1):
            s = set(nums[i:i+k])
            for x in s:
                c[x]+=1
        for x in c:
            if c[x]==1:
                ans=max(ans,x)
        return ans