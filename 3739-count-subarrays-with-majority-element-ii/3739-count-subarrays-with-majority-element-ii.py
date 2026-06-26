class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        p = [0]*(n*2+1)
        p[n] = 1
        c = n
        ans = ps = 0
        for i in range(n):
            if nums[i]==target:
                ps+=p[c]
                c +=1
                p[c]+=1
            else:
                c-=1
                ps-=p[c]
                p[c]+=1
            ans+=ps
        return ans