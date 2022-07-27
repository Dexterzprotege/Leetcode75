# Question: https://leetcode.com/problems/number-of-islands/

# Solution:
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        ans = 0
        
        def dfs(row, col):
            if row < 0 or col < 0 or row >= ROW or col >= COL or grid[row][col] == '0':
                return 
            grid[row][col] = "0"
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
            
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == "1":
                    dfs(i, j)
                    ans += 1
                    
        return ans
      
# Verdict:
# Runtime: 437 ms, faster than 61.46% of Python3 online submissions for Number of Islands.
# Memory Usage: 16.5 MB, less than 63.92% of Python3 online submissions for Number of Islands.
