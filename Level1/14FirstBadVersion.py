# Question; https://leetcode.com/problems/first-bad-version/

# Solution:
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            mid = left + (right-left)//2
            if isBadVersion(mid) == False:
                left = mid + 1
            else:
                right = mid - 1
        return left
      
# Verdict:
# Runtime: 47 ms, faster than 46.55% of Python3 online submissions for First Bad Version.
# Memory Usage: 13.9 MB, less than 60.97% of Python3 online submissions for First Bad Version.
