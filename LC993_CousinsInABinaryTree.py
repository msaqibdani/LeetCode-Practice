'''

In a binary tree, the root node is at depth 0, 
and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, 
but have different parents.

We are given the root of a binary tree with unique values, 
and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding
 to the values x and y are cousins.

 

Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:



Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false


'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

    q = deque()
    q.append((root, TreeNode('a'), 1))
    found = {}

    while q:
        curr_node, parent, depth = q.popleft()
        
        if curr_node != None:
            if curr_node.val == x or curr_node.val == y:
                found[curr_node.val] = (parent.val, depth)
        
        if x in found and y in found:
            
            if found[x][0] != found[y][0] and found[x][1] == found[y][1]:
                return True
            
            else:
                return False
        
        if curr_node.left:
            q.append((curr_node.left, curr_node, depth+1))
        
        if curr_node.right:
            q.append((curr_node.right, curr_node, depth+1))


    return False        