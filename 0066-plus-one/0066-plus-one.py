class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:#[1,2,3]
        n=int("".join(map(str,digits)))+1
        return [int(i) for i in str(n)]
        