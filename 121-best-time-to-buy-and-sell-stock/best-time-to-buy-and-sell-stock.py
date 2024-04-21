class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        price_min = float('inf')
        profit_max = 0

        for i in range(len(prices)):
            if prices[i] < price_min:
                price_min = prices[i]

            elif prices[i] - price_min > profit_max:
                profit_max = prices[i] - price_min

        return profit_max