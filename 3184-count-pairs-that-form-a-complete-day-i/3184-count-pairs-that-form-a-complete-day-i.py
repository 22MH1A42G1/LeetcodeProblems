class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        c=0
        for i in range(len(hours)):
            for j in range(i+1,len(hours)):
                if (hours[i]+hours[j])%24==0:
                    c+=1
        return c