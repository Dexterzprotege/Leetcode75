# Question: https://leetcode.com/problems/unique-paths/

# Code:
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n] * m
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
      
# Verdict:
# Runtime: 56 ms, faster than 31.08% of Python3 online submissions for Unique Paths.
# Memory Usage: 14 MB, less than 32.87% of Python3 online submissions for Unique Paths.
