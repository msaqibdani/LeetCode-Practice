
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def getNeighbors(row, col, grid):
            
            change = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            nei = []
            
            for x, y in change:
                
                new_row = row+x
                new_col = col+y
                
                if new_row >= 0 and new_row < len(grid) and new_col >= 0 and new_col < len(grid[0]):
                    nei.append((new_row, new_col))
            
            return nei
        
        def dfs(row, col, visited):
            
            stack = []
            stack.append((row, col))
            visited.add((row, col))
            
            while stack:
    
                curr_r, curr_c = stack.pop()
                
                neighbors = getNeighbors(curr_r, curr_c, grid)
                
                for r, c in neighbors:
                    
                    if (r, c) not in visited and grid[r][c] == "1":
                        stack.append((r, c))
                        visited.add((r, c))
            
        count = 0
        visited = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j, visited)
                    count+=1
        
        
        return count
    
    

