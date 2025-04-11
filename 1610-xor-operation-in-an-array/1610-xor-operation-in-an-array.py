class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        c = start + 2 * 0
        for i in range(1,n):
            c^= start + 2 * i
        return c