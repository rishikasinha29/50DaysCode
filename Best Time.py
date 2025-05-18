from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        You are given an array prices where prices[i] is the price of a given stock on the ith day.
        You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
        Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

        Example 1:
        Input: prices = [7,1,5,3,6,4]
        Output: 5
        Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
        Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

        Example 2:
        Input: prices = [7,6,4,3,1]
        Output: 0
        Explanation: In this case, no transactions are done and the max profit = 0.

        Constraints:
        1 <= prices.length <= 10^5
        0 <= prices[i] <= 10^4
        """
        if not prices or len(prices) < 2:
            return 0

        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
            if price < min_price:
                min_price = price

        return max_profit

# Example Usage:
solution = Solution()
prices1 = [7, 1, 5, 3, 6, 4]
print(f"Maximum profit for prices {prices1}: {solution.maxProfit(prices1)}")

prices2 = [7, 6, 4, 3, 1]
print(f"Maximum profit for prices {prices2}: {solution.maxProfit(prices2)}")

prices3 = [2, 4, 1]
print(f"Maximum profit for prices {prices3}: {solution.maxProfit(prices3)}")

prices4 = [2, 1, 4]
print(f"Maximum profit for prices {prices4}: {solution.maxProfit(prices4)}")
