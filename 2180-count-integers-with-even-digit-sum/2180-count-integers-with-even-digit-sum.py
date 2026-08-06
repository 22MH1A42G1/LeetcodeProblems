class Solution:
    def countEven(self, num: int) -> int:
        return (num - sum(map(int, str(num)))%2)//2