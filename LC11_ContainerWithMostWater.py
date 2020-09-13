class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l, r, global_area = 0, len(height) - 1, 0
        
        while l < r:
            
            curr_h = min(height[l], height[r])
            curr_w = r - l
    
            area = curr_h * curr_w
            global_area = max(area, global_area)
        
            if height[l] >= height[r]:
                r -= 1
            
            else:
                l += 1
        
        
        return global_area
        
        
        
        
        
        
        
        
        
        
        
        