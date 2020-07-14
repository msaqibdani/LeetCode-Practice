class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[-1 for i in range(n)] for j in range(m)]
        
        def helper(row, col):
            
            if row == m-1 and col == n-1:
                return 1
            
            if dp[row][col] != -1:
                return dp[row][col]
            
            temp = 0
            for x, y in [[1, 0], [0, 1]]:
                
                new_row = row + x
                new_col = col + y
                
                if new_row >= 0 and new_row < m and new_col >= 0 and new_col < n:
                    temp += helper(new_row, new_col)
            
            dp[row][col] = temp
            return temp
        
        return helper(0, 0)
                