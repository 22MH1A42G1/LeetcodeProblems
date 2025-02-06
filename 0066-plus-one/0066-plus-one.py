class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:#[1,2,3]
        # n = len(digits)#3
        # for i in range(n - 1, -1, -1):#2,-1,--
        #     digits[i] += 1
        #     if digits[i] < 10:
        #         return digits
        #     digits[i] = 0
        # return [1] + digits
        d = "".join(map(str,digits))
        e = int(d)
        f = e + 1
        h = list(str(f))
        g = [int(i) for i in h]
        return g