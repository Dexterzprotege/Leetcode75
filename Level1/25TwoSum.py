# Question: https://leetcode.com/problems/two-sum/

# Solution:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in dic:
                return [dic[diff], i]
            else:
                dic[nums[i]] = i
                
# Verdict:
# Runtime: 100 ms, faster than 60.69% of Python3 online submissions for Two Sum.
# Memory Usage: 15.3 MB, less than 14.30% of Python3 online submissions for Two Sum.
