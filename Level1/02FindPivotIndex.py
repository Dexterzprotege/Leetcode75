# Question: https://leetcode.com/problems/find-pivot-index/

# Solution:
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        summ = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            rightSum = summ - leftSum - nums[i]
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1

# Verdict:
# Runtime: 214 ms, faster than 65.15% of Python3 online submissions for Find Pivot Index.
# Memory Usage: 15.2 MB, less than 48.62% of Python3 online submissions for Find Pivot Index.
