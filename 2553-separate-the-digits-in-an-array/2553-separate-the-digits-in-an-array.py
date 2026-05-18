class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        d = []
        for i in nums:
            num = str(i)
            for j in num:
                d.append(int(j))
        return(d)