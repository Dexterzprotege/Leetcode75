# Question: https://leetcode.com/problems/is-subsequence/

# Solution 1: Brute Force (2 Pointer)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
      
# Verdict:
# Runtime: 54 ms, faster than 45.06% of Python3 online submissions for Is Subsequence.
# Memory Usage: 13.9 MB, less than 82.20% of Python3 online submissions for Is Subsequence.
