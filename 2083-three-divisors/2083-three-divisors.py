class Solution:
    def isThree(self, n: int) -> bool:
        c = 1
        x = n//2+1
        for i in range(1,x):
            if n%i == 0:
                c += 1
        if c == 3:
            return True
        else:
            return False