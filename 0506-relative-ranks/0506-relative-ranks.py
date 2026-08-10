class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        l = []
        t = sorted(score)[::-1]
        print(t)
        for i in range(len(t)):
            if score[i]==t[0]:
                l.append("Gold Medal")
            elif score[i]==t[1]:
                l.append("Silver Medal")
            elif score[i]==t[2]:
                l.append("Bronze Medal")
            else:
                l.append(str(t.index(score[i])+1))
        return l