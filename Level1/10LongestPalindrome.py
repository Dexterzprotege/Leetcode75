# Question: https://leetcode.com/problems/longest-palindrome/

# Solution:
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter()
        for c in s:
            count[c] += 1
        
        ans = 0
        oddFound = False
        
        for c in count:
            if count[c] % 2 == 0:
                ans += count[c]
            else:
                oddFound = True
                ans += count[c] - 1
        
        return ans if oddFound is False else ans + 1
      
# Verdict:
# Runtime: 57 ms, faster than 35.84% of Python3 online submissions for Longest Palindrome.
# Memory Usage: 13.8 MB, less than 65.66% of Python3 online submissions for Longest Palindrome.
