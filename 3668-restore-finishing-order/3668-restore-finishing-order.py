class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        return [i for i in order if i in friends]