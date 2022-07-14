# Question: https://leetcode.com/problems/running-sum-of-1d-array/

# Solution:
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums

# Verdict:
# Runtime: 51 ms, faster than 74.36% of Python3 online submissions for Running Sum of 1d Array.
# Memory Usage: 14 MB, less than 71.01% of Python3 online submissions for Running Sum of 1d Array.
