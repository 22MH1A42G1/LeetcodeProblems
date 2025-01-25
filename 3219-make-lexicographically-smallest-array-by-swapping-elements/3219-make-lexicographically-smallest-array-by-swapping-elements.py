class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        help_list = [(nums[i], i) for i in range(n)]
        help_list.sort(key=lambda x: x[0])
        
        res = [0] * n
        prev = float('-inf')
        pos = []
        
        s = 0
        e = 0
        while e < n:
            pos.append(help_list[e][1])
            prev = help_list[e][0]
            e += 1
            if e == n or help_list[e][0] - prev > limit:
                pos.sort()
                for idx in pos:
                    res[idx] = help_list[s][0]
                    s += 1
                pos.clear()
        
        return res