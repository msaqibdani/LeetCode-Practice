class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        
        '''
        0. starting no overlap GOOD
        1. starting overlap GOOD
        
        2. ending no overlap GOOD
        3. ending overlap GOOD
        
        4. starting in middle and multiple overlaps GOOD
        5. starting in middle and ending after one overlap GOOD
        
        6. starting between 2 and multiple overlaps
        7. starting between 2 and ending after one overlap
        
        '''
        
        output = []
        new_start, new_end = newInterval
        idx, n = 0, len(intervals)
        
        while idx < n and new_start > intervals[idx][0]:
            output.append(intervals[idx])
            idx += 1
        
        #if no overlap
        if not output or output[-1][1] < new_start:
            output.append(newInterval)
        
        #if there's an overlap
        else:
            output[-1][1] = max(output[-1][1], new_end)
        
        
        while idx < n:
            start, end = intervals[idx]
            idx += 1
            
            
            #if no overlap
            if output[-1][1] < start:
                output.append([start, end])
            
            else:
                output[-1][1] = max(output[-1][1], end)
        
        
        return output
        
        
                
            
            
        
            
            
        
            
            