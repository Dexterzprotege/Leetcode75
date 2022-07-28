# Question: https://leetcode.com/problems/longest-repeating-character-replacement/

# Code:
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        res = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] += 1
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
      
# Solution:
# Runtime: 243 ms, faster than 36.83% of Python3 online submissions for Longest Repeating Character Replacement.
# Memory Usage: 14 MB, less than 19.59% of Python3 online submissions for Longest Repeating Character Replacement.
