class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        fa = []
        for i in order:
            if i in friends:
                fa.append(i)
        return fa