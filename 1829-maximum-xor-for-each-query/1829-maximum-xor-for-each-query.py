class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        ans, mx, xor = [], (1 << maximumBit) - 1, 0
        for num in nums:
            xor ^= num
            ans.append(xor ^ mx)
        return ans[:: -1]