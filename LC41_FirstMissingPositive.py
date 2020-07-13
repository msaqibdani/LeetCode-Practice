class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        #check if 1 is available
        for num in nums:
            if num == 1:
                break
        
        else:
            return 1
        
        #data cleanup
        for i, num in enumerate(nums):
            if num <= 0 or num > len(nums):
                nums[i] = 1
        
        #converting signs for each num available
        for i, num in enumerate(nums):
            
            index = abs(num)
            
            if index == len(nums): nums[0] = - abs(nums[0])
            else: nums[index] = - abs(nums[index])
        
        #check first positive
        for i in range(1, len(nums)):
            if nums[i] > 0:
                return i
        
        if nums[0] > 0:
            return len(nums)
        
        return len(nums)+1
                
    