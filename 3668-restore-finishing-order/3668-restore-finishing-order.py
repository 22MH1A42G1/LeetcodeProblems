class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        s=set(friends)
        return [i for i in order if i in s]