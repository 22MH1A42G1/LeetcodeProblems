class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        return any(2 * x in cnt and x != 0 for x in arr) or cnt[0] > 1