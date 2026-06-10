class SegTree:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.maxv = [0] * (4 * self.n)
        self.minv = [0] * (4 * self.n)
        self.build(1, 0, self.n - 1, nums)

    def build(self, node: int, l: int, r: int, nums: List[int]):
        if l == r:
            self.maxv[node] = self.minv[node] = nums[l]
            return
        m = (l + r) // 2
        self.build(node * 2, l, m, nums)
        self.build(node * 2 + 1, m + 1, r, nums)
        self.maxv[node] = max(self.maxv[node * 2], self.maxv[node * 2 + 1])
        self.minv[node] = min(self.minv[node * 2], self.minv[node * 2 + 1])

    def queryMax(self, node: int, l: int, r: int, ql: int, qr: int) -> int:
        if ql <= l and r <= qr:
            return self.maxv[node]
        m = (l + r) // 2
        res = -(10**18)
        if ql <= m:
            res = max(res, self.queryMax(node * 2, l, m, ql, qr))
        if qr > m:
            res = max(res, self.queryMax(node * 2 + 1, m + 1, r, ql, qr))
        return res

    def queryMin(self, node: int, l: int, r: int, ql: int, qr: int) -> int:
        if ql <= l and r <= qr:
            return self.minv[node]
        m = (l + r) // 2
        res = 10**18
        if ql <= m:
            res = min(res, self.queryMin(node * 2, l, m, ql, qr))
        if qr > m:
            res = min(res, self.queryMin(node * 2 + 1, m + 1, r, ql, qr))
        return res


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        seg = SegTree(nums)
        pq = [
            (
                -(
                    seg.queryMax(1, 0, n - 1, l, n - 1)
                    - seg.queryMin(1, 0, n - 1, l, n - 1)
                ),
                l,
                n - 1,
            )
            for l in range(n)
        ]
        heapq.heapify(pq)
        ans = 0
        while k:
            negVal, l, r = heapq.heappop(pq)
            ans -= negVal
            k -= 1
            if r > l:
                heapq.heappush(
                    pq,
                    (
                        -(
                            seg.queryMax(1, 0, n - 1, l, r - 1)
                            - seg.queryMin(1, 0, n - 1, l, r - 1)
                        ),
                        l,
                        r - 1,
                    ),
                )
        return ans