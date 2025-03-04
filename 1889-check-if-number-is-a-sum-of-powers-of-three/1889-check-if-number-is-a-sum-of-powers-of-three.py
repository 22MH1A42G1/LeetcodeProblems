class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        return self.f(0, n)
    def f(self, power: int, n: int) -> bool:
        if n == 0:
            return True
        if 3**power > n:
            return False
        add_power = self.f(power + 1, n - 3**power)
        skip_power = self.f(power + 1, n)
        return add_power or skip_power