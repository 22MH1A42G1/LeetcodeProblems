class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0 or ((math.log(n,4) % 1.0) != 0.0):
            return False
        else:
            return True