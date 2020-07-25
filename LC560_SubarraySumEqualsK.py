class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0: 1}
        
        
        cum_sum, count = 0, 0
        
        for num in nums:
            
            cum_sum += num
            
            if cum_sum - k in hashmap:
                count += hashmap[cum_sum-k]
            
            hashmap[cum_sum] = hashmap.get(cum_sum, 0) + 1
    
        return count
        