class Solution:
    def leftmostBuildingQueries(self, h: List[int], q: List[List[int]]) -> List[int]:
        m, r, s = [], [-1]*len(q), [[] for _ in h]
        for i, j in enumerate(q):
            a, b = j
            if a < b and h[a] < h[b]: r[i] = b
            elif a > b and h[a] > h[b]: r[i] = a
            elif a == b: r[i] = a
            else: s[max(a, b)].append((max(h[a], h[b]), i))
        for i, j in enumerate(h):
            while m and m[0][0] < j:
                _, qi = heapq.heappop(m)
                r[qi] = i
            for k in s[i]: heapq.heappush(m, k)
        return r