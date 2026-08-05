from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = Counter(s)
        if not counts:
            return True
        first_count = next(iter(counts.values()))
        return all(count == first_count for count in counts.values())