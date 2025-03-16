class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l,h=1,cars*cars*ranks[0]
        while l<h:
            m=(l+h)//2
            c=sum(int((m/r)**0.5) for r in ranks)
            if c<cars:
                l=m+1
            else:
                h=m
        return l