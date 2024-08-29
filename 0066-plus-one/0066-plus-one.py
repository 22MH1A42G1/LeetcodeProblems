class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=int(''.join(map(str,digits)))
        m=n+1
        l=[int(i) for i in str(m)]
        return l