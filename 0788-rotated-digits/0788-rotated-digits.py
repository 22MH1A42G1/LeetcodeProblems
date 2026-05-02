class Solution:
    def rotatedDigits(self, n: int) -> int:
        res = 0
        for num in range(1, n + 1):
            curr = str(num)
            if "3" in curr or "4" in curr or "7" in curr:
                continue
            if "2" in curr or "5" in curr or "9" in curr or "6" in curr:
                res += 1
        return res
