'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

def subsets(self, nums: List[int]) -> List[List[int]]:

    final = [[]]

    def helper(index, ls):
        if index >= len(nums):
            return
        
        for i in range(index, len(nums)):
            
            ls.append(nums[i])
            final.append(ls[:])
            helper(i+1, ls)
            ls.pop()

    helper(0, [])
    return final
        
        