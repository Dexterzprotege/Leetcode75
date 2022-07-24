# Question: https://leetcode.com/problems/fibonacci-number

# Solution
class Solution:
    def fib(self, n: int) -> int:
        phi = (5**0.5 + 1) / 2
        return round(phi**n / 5**0.5)
      
# Verdict:
# Runtime: 45 ms, faster than 67.70% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 14 MB, less than 9.48% of Python3 online submissions for Fibonacci Number.
