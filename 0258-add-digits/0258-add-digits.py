class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            addDigits = 0
            for digit in str(num):
                addDigits += int(digit)
            num = addDigits
        return num
