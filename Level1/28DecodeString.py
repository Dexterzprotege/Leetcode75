# Question: https://leetcode.com/problems/decode-string/

# Solution:
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            if s[i] != ']':
                stack.append(s[i])
            else:
                tmp = ""
                while stack and stack[-1] != '[':
                    tmp = stack.pop() + tmp
                stack.pop()
                
                counter = ""
                while stack and stack[-1].isdigit():
                    counter = stack.pop() + counter
                stack.append(int(counter)*tmp)
            i += 1
        return ''.join(stack)
      
# Verdict:
# Runtime: 41 ms, faster than 68.16% of Python3 online submissions for Decode String.
# Memory Usage: 13.9 MB, less than 71.37% of Python3 online submissions for Decode String.
