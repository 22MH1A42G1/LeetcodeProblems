class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year, month, day = map(int, date.split('-'))
        return f"{year:b}-{month:b}-{day:b}"