from collections import Counter
class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        l = order+friends
        ans = []
        d = Counter(l)
        for i,j in d.items():
            if j==2:
                ans.append(i)
        return ans