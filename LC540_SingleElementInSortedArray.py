def singleNonDuplicate(self, nums: List[int]) -> int:
    
    l, r = 0, len(nums)-1
    
    while l < r:
        
        mid = l + (r-l)//2
        halves_are_even = (r - mid) % 2 == 0
        
        if nums[mid] == nums[mid+1]:
            
            if halves_are_even:
                l = mid + 2
            else:
                r = mid - 1
        
        elif nums[mid-1] == nums[mid]:
            
            if halves_are_even:
                r = mid - 2
            else:
                l = mid + 1
            
        
        else:
            return nums[mid]
    
    return nums[l]

            
            
        
        