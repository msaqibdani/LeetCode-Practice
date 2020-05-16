def maxSubarraySumCircular(self, A: List[int]) -> int:
    
    total = local_max = local_min = 0
    maximum = float('-inf')
    minimum = float('inf')
    
    
    for num in A:
        
        total += num
        
        local_max = max(num, local_max + num)
        local_min = min(num, local_min + num)
        
        maximum = max(maximum, local_max)
        minimum = min(minimum, local_min)
    
    
    if maximum > 0:
        return max(maximum, total - minimum)
    
    else:
        return maximum
    
    
    
            
        
    
    
    
    
    