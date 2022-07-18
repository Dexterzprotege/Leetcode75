# Question: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Solution:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        maxProfit = 0
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                maxProfit = max(maxProfit, prices[sell] - prices[buy])
            else:
                buy += 1
            sell += 1
        return maxProfit
      
# Verdict:
# Runtime: 2327 ms, faster than 5.74% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 25.1 MB, less than 37.97% of Python3 online submissions for Best Time to Buy and Sell Stock.
