class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum = [0]*(len(gain)+1)
        for i in range(1,len(gain)+1):
            prefix_sum[i] = prefix_sum[i-1] + gain[i-1]
        # print(prefix_sum)
        return max(prefix_sum)