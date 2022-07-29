# Question: https://leetcode.com/problems/bulls-and-cows/

# Solution:
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A = 0
        bucket = [0] * 10
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A += 1
            bucket[int(secret[i])] += 1  
            bucket[int(guess[i])] -= 1
        
        # Cows is: Total length of secret - Common elements - Matched elememts
        B = len(secret) - A - sum(cnt for cnt in bucket if cnt>0)
        return str(A) + "A" + str(B) + "B"
      
# Verdict:
# Runtime: 56 ms, faster than 67.39% of Python3 online submissions for Bulls and Cows.
# Memory Usage: 13.9 MB, less than 78.40% of Python3 online submissions for Bulls and Cows.
