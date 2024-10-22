class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lower=float("+inf")
        diff=0
        for price in prices:
            if price<=lower:
                lower=price
            else:
                diff=max(diff,price-lower)
        return diff