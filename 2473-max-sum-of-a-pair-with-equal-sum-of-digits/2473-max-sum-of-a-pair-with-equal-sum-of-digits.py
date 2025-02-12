class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d, mx = dict(), -1
        for num in nums:
            sm, n = 0, num
            while n:
                sm += n % 10
                n //= 10
            if sm in d:
                if d[sm][0] <= num:
                    d[sm][1] = d[sm][0]
                    d[sm][0] = num
                elif d[sm][1] < num:
                    d[sm][1] = num
            else:
                d[sm] = [num, -1]
        for k in d:
            if d[k][1] != -1: 
                sm = d[k][0] + d[k][1]
                if sm > mx:
                    mx = sm
        return mx