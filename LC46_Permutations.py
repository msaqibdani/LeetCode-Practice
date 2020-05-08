'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

'''


def permute(self, nums: List[int]) -> List[List[int]]:

    final = []

    def helper(ls, soFar):
        
        if len(ls) == len(nums):
            final.append(ls[:])
            return
        
        
        for ele in nums:
            
            if ele not in soFar:
                ls.append(ele)
                soFar.add(ele)
                helper(ls, soFar)
                
                ls.pop()
                soFar.remove(ele)


    helper([], set())
    return final
            
        
        