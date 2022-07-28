# Question: https://leetcode.com/problems/find-all-anagrams-in-a-string/

# Code:
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def ctoi(c):
            return ord(c) - ord('a')
        
        lenP, lenS = len(p), len(s)
        if lenP > lenS: return []
        pCount, sCount = [0] * 26, [0] * 26
        for i in range(lenP):
            pCount[ctoi(p[i])] += 1
            sCount[ctoi(s[i])] += 1

        res = [0] if pCount == sCount else []
        

        for i in range(lenP, lenS):
            sCount[ctoi(s[i-lenP])] -= 1
            sCount[ctoi(s[i])] += 1
            
            if sCount == pCount:
                res.append(i-lenP+1)
                
        return res            
      
# Solution:
# Runtime: 187 ms, faster than 60.90% of Python3 online submissions for Find All Anagrams in a String.
# Memory Usage: 15.2 MB, less than 33.28% of Python3 online submissions for Find All Anagrams in a String.
