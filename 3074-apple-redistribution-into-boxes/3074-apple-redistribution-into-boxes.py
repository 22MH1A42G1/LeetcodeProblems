class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        t=sum(apple)
        c=0
        while t>0:
            t-=capacity[c]
            c+=1
        return c