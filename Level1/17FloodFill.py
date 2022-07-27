# Question: https://leetcode.com/problems/flood-fill/submissions/

# Solution:
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROW, COL = len(image), len(image[0])
        currColor = image[sr][sc]
        if color == currColor:
            return image
        def dfs(row, col):
            if row < 0 or col < 0 or row >= ROW or col >= COL or image[row][col] != currColor:
                return
            image[row][col] = color
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
        dfs(sr, sc)
        return image
      
# Verdict:
# Runtime: 79 ms, faster than 92.41% of Python3 online submissions for Flood Fill.
# Memory Usage: 14.2 MB, less than 14.04% of Python3 online submissions for Flood Fill.
