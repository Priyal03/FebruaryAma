class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minPrice = float("inf")
        maxProfit = 0

        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]

            else:
                profit = prices[i] - minPrice
                if profit > maxProfit:
                    maxProfit = profit

        return maxProfit

# best solution O(n) and space O(1)