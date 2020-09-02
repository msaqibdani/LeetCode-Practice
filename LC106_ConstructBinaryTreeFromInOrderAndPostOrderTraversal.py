class TreeNode():
  def __init__(self, val):
    self.val = val
    self.right = None
    self.left = None
  

def buildTree(inorder, postorder):
  
  def helper(left, right):
    
    if left > right:
      return None
      
    
    #popping the last element
    root = postorder.pop()
    #creating the node
    treeRoot = TreeNode(root)
    #index value in inorder
    index_value = indexes[root]
    
    
    treeRoot.right = helper(index_value+1, right)
    treeRoot.left = helper(left, index_value-1)
    
    return treeRoot

  indexes = {key:value for value, key in enumerate(inorder)}
  return helper(0, len(inorder) - 1)
