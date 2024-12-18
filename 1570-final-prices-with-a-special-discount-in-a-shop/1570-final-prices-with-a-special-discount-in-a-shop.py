class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        r = prices.copy()
        n = len(prices)
        for i in range(n):
            for j in range(i+1,n):
                if prices[j] <= prices[i]:
                    r[i] = prices[i]-prices[j]
                    break
        return r