# Question: https://leetcode.com/problems/isomorphic-strings/

# Solution:
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        for i in range(len(s)):
            if s[i] in dic:
                if dic[s[i]] != t[i]:
                    return False
            else:
                if t[i] in dic.values():
                    return False
                else:
                    dic[s[i]] = t[i]
        return True
      
# Verdict:
# Runtime: 39 ms, faster than 95.65% of Python3 online submissions for Isomorphic Strings.
# Memory Usage: 14.1 MB, less than 88.65% of Python3 online submissions for Isomorphic Strings.
