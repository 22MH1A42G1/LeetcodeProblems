class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        #print(c)
        l = []
        for i,j in c.items():
            if j==2:
                l.append(i)
        return l