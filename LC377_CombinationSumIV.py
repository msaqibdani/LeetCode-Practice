class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
    
        dp = {}
        
        def helper(rem):
            
            if rem < 0:
                return 0
            
            elif rem == 0:
                return 1
            
            elif rem in dp:
                return dp[rem]
                
            temp = 0
            for ele in nums:
                
                rem -= ele
                temp += helper(rem)
                rem += ele
            
            dp[rem] = temp
            return temp
        
        return helper(target)
            
            
                
                
        