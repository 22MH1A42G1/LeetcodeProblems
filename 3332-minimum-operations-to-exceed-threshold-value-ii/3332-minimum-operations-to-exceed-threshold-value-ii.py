class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        res=0
        for i in range(0, len(nums)):
            x=heapq.heappop(nums)
            if x<k:
                res+=1
                y=heapq.heappop(nums)
                val= x*2+y if (x<y) else y*2+x
                heapq.heappush(nums, val)
            else:
                break
        return res
