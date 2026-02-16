class Solution:
    def reverseBits(self, n: int) -> int:
        s=format(n,'032b')
        #print(s)
        s=s[::-1]
        #print(s)
        n1=int(s,2)
        return n1