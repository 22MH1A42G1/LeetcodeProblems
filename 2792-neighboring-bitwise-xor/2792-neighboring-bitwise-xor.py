class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        c=0
        for i in derived:
            c^=i
        return True if c==0 else False