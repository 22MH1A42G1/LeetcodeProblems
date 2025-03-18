class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        d = dict(zip(heights, names))
        s = sorted(heights, reverse=True)
        l = []
        for i in s:
            l.append(d[i])
        return l