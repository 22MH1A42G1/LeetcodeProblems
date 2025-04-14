class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        return sum(abs(v-u)<=a and abs(u-w)<=b and abs(v-w)<=c for v,u,w in combinations(arr,3))