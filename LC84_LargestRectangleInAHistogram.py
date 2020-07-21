class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        if not heights: return 0
        
        stack = [-1]
        i, n, area = 0, len(heights), 0
        
        for i in range(n):
            
            #if the last element in the stack >= curr_element
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                
                curr_height = heights[stack.pop()]
                width = i - stack[-1]-1
                
                area = max(area, curr_height * width)
            
            stack.append(i)
        
        #if there are elements left in the stack
        while stack[-1] != -1:
            curr_height = heights[stack.pop()]
            width = n - stack[-1]-1
            area = max(area, curr_height * width)
        
        return area
        
        
                    
        
        
        
