class Solution:
    def maxAverageRatio(self, A: List[List[int]], k: int) -> float:
        h = [(a / b - (a + 1) / (b + 1), a, b) for a, b in A]
        heapify(h)
        while k:
            v, a, b = heapq.heappop(h)
            a, b = a + 1, b + 1
            heapq.heappush(h, (-(a + 1) / (b + 1) + a / b, a, b))
            k -= 1
        return sum(a / b for v, a, b in h) / len(h)