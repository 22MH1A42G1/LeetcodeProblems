class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr.sort()
        u = set()
        c = 1
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                c += 1
            else:
                if c in u:
                    return False
                u.add(c)
                c = 1
        if c in u:
            return False
        return True