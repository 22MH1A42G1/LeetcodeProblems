class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sum_arr = [0] * (n + 1)
        
        for i in range(n):
            sum_arr[i + 1] = sum_arr[i] + nums[i]
        
        q = [0] * (n + 1)
        l = r = 0
        min_length = n + 1
        
        for i in range(len(sum_arr)):
            while r > l and sum_arr[i] >= sum_arr[q[l]] + k:
                min_length = min(min_length, i - q[l])
                l += 1
            
            while r > l and sum_arr[i] <= sum_arr[q[r - 1]]:
                r -= 1
            
            q[r] = i
            r += 1
        
        return min_length if min_length <= n else -1