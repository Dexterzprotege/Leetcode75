# Question: https://leetcode.com/problems/binary-search/

# Solution:
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1
      
# Verdict:
# Runtime: 538 ms, faster than 5.05% of Python3 online submissions for Binary Search.
# Memory Usage: 15.4 MB, less than 97.45% of Python3 online submissions for Binary Search.
