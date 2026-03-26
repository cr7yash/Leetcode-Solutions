class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest_price = float("inf")
        max_price = 0

        for price in prices:
            if price > cheapest_price:
                max_price = max(max_price,price - cheapest_price)
            else:
                cheapest_price = price                
        return max_price

        