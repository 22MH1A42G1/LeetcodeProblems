class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        import math
        sumOdd = 0
        sumEven = 0
        for i in range(1, (2*n)+1):
            if i%2 == 0:
                sumEven += i
            else:
                sumOdd += i
        # print(sumOdd)
        # print(sumEven)
        return math.gcd(sumOdd, sumEven)