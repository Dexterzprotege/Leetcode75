# Question: https://leetcode.com/problems/climbing-stairs/

# Solution:
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 1]
        for i in range(2, n+1):
            dp.append(dp[i-1]+dp[i-2])
        return dp[n]
      
# Verdict:
# Runtime: 41 ms, faster than 64.78% of Python3 online submissions for Climbing Stairs.
# Memory Usage: 13.8 MB, less than 96.04% of Python3 online submissions for Climbing Stairs.
