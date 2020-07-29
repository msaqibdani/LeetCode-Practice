class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
  
  
        left, right = len(nums), 0
        stack = []
        
        for i, num in enumerate(nums):
            
            while stack and nums[stack[-1]] > num:
                left = min(left, stack.pop())
            stack.append(i)
        
        stack = []
        
        for j in range(len(nums)-1, -1, -1):
            
            while stack and nums[stack[-1]] < nums[j]:
                right = max(right, stack.pop())
            stack.append(j)
        
        
        
        if right - left > 0:
            return right - left + 1
        else:
            return 0
