class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        ha = 30*hour + 0.5*minutes
        ma = 6*minutes
        return min(360-abs(ha-ma),abs(ha-ma))