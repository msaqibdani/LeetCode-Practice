# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def isValidBST(self, root: TreeNode) -> bool:
    
    def helper(node, left, right):
        
        if not node:
            return True
        
        if node.val <= left or node.val >= right:
            return False
        
        left_root = helper(node.left, left, node.val)
        right_root = helper(node.right, node.val, right)
        
        
        
        if left_root and right_root:
            return True
        
        return False
            
    
    return helper(root, float('-inf'), float('inf'))
        