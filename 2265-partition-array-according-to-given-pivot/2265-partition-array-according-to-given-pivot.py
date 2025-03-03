class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l=[]
        g=[]
        e=[]
        for i in nums:
            if i < pivot:
                l.append(i)
            elif i > pivot:
                g.append(i)
            else:
                e.append(i)
        l.extend(e)
        l.extend(g)
        return l