# Question: https://leetcode.com/problems/min-cost-climbing-stairs/

# Solution:
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a, b = cost[0], cost[1]
        for i in range(2, len(cost)):
            a, b = b, cost[i] + min(a, b)
        return min(a, b)
      
# Verdict:
# Runtime: 113 ms, faster than 22.66% of Python3 online submissions for Min Cost Climbing Stairs.
# Memory Usage: 13.9 MB, less than 97.18% of Python3 online submissions for Min Cost Climbing Stairs.
