from functools import lru_cache
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        melidroni = (num1, num2)
        def count_upto(x: int) -> int:
            if x < 0:
                return 0
            digits = list(map(int, str(x)))
            n = len(digits)
            @lru_cache(None)
            def dp(pos: int, tight: int, prev2: int, prev1: int, leading: int):
                if pos == n:
                    return (1, 0)   
                limit = digits[pos] if tight else 9
                total_count = 0
                total_wav = 0
                for d in range(0, limit + 1):
                    ntight = tight and (d == limit)
                    nleading = leading and (d == 0)
                    if nleading:
                        npc2, npc1 = 10, 10
                        contrib = 0
                    elif prev1 == 10:
                        npc2, npc1 = 10, d
                        contrib = 0
                    elif prev2 == 10:
                        npc2, npc1 = prev1, d
                        contrib = 0
                    else:
                        is_peak = (prev1 > prev2 and prev1 > d)
                        is_valley = (prev1 < prev2 and prev1 < d)
                        contrib = 1 if (is_peak or is_valley) else 0
                        npc2, npc1 = prev1, d
                    cnt_sub, wav_sub = dp(pos + 1, 1 if ntight else 0, npc2, npc1, 1 if nleading else 0)
                    total_count += cnt_sub
                    total_wav += wav_sub + contrib * cnt_sub
                return (total_count, total_wav)
            return dp(0, 1, 10, 10, 1)[1]
        return count_upto(num2) - count_upto(num1 - 1)