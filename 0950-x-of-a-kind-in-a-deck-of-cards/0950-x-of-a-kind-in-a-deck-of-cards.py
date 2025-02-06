from collections import Counter
from typing import List
from math import gcd
from functools import reduce

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        c = Counter(deck)
        values = list(c.values())
        X = reduce(gcd, values)
        return X >= 2
