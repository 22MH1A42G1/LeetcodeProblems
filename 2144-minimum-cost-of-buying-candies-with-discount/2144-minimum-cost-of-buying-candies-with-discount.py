class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        cost[:]=cost[::-1]
        res = 0
        for i in range(len(cost)):
            if i%3!=2: 
                res +=cost[i]
        return res