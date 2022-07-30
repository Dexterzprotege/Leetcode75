# Question: https://leetcode.com/problems/backspace-string-compare/

# Solution: Two stacks
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for c in s:
            if c != '#':
                stack1.append(c)
            elif stack1:
                stack1.pop()
        for c in t:
            if c != '#':
                stack2.append(c)
            elif stack2:
                stack2.pop()
        
        return stack1 == stack2

# Verdict:
# Runtime: 42 ms, faster than 70.00% of Python3 online submissions for Backspace String Compare.
# Memory Usage: 13.8 MB, less than 74.23% of Python3 online submissions for Backspace String Compare.
