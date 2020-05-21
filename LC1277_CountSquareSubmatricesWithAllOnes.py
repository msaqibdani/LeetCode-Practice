class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])
        count = sum(matrix[0])
        
        for i in range(1, ROWS):
            for j in range(COLS):
                
                if j == 0:
                    count += matrix[i][j]
                    
                elif matrix[i][j] == 0:
                    continue
                
                elif matrix[i][j] == 1:
                    matrix[i][j] = min(matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1]) + 1
                    count += matrix[i][j]
                
                
        return count
                