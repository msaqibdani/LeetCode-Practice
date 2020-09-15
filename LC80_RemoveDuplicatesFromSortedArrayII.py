class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        '''
        
        [1, 1, 2, x, 2, x, 3, 3, x, x, 4]
                     k
                  i
         
        '''
        
        if not nums: return 0
        
        element = nums[0]
        freq = 0
        total = 0
        
        
        for idx, num in enumerate(nums):
            
            if num == element:
                freq += 1
            
            else:
                element = num
                freq = 1
            
            if freq > 2:
                nums[idx] = 'x'
            
            else:
                total += 1
        
        
        replace = 0
        j = 0
        
        while j < len(nums) and nums[j] != 'x':
            j += 1
            replace += 1
        
        while j < len(nums):
            
            if nums[j] != 'x':
                nums[j], nums[replace] = nums[replace], nums[j]
                replace += 1
            
            j += 1
        
        
        return total
            
            
                
                
        
        
        
        