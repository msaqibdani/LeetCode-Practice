from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
  
        if not root: return []
        
        q = deque()
        ans = []
        q.append(root)
        
        
        while q:
        
            ans.append(q[-1].val)
            q = [y for x in q for y in [x.left, x.right] if y]
        
        return ans
            
            
            