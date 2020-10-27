from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        '''
        Add all rotten oranges to q
        do a bfs, track time 
        return time
        '''
        def getNeighbors(r, c):
            ans = []
            delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            
            for x, y in delta:
                new_r = r + x
                new_c = c + y
                
                if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] == 1:
                    ans.append((new_r, new_c))
            
            return ans
                    
        
        q = deque()
        total_unrotten = 0
        #visited = set() -> Do not really need a visited set as I can change the input grid
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                
                elif grid[i][j] == 1:
                    total_unrotten += 1
    
        curr_time = 0
        while q:
            
            r, c, curr_time = q.popleft()
            
            neighbors = getNeighbors(r, c)
            
            for row, col in neighbors:
                grid[row][col] = 2
                total_unrotten -= 1
                q.append((row, col, curr_time + 1))
        
        
        return curr_time if total_unrotten == 0 else -1