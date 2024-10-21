class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        lower=prices[0]
        profit=0
        for price in prices:
            lower=min(lower,price)
            profit=max(profit,price-lower)
        return profit