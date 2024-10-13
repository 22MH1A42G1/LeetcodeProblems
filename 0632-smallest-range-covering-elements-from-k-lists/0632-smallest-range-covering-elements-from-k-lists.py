import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        mh = []
        cm = float('-inf')
        for i in range(len(nums)):
            heapq.heappush(mh, (nums[i][0], i, 0))
            cm = max(cm, nums[i][0])
        rr = [-10**5, 10**5]
        while mh:
            mi, li, ei = heapq.heappop(mh)
            if cm - mi < rr[1] - rr[0]:
                rr = [mi, cm]
            if ei + 1 == len(nums[li]):
                break
            ne = nums[li][ei + 1]
            heapq.heappush(mh, (ne, li, ei + 1))
            cm = max(cm, ne) 
        return rr