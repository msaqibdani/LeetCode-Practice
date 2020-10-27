# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict, deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        
        graph = defaultdict(list)
        
        def createGraph(node):
            
            if not node:
                return
            
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                createGraph(node.left)
            
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                createGraph(node.right)
        
        createGraph(root)
        
        
        ans = []
        q = deque()
        q.append((target.val, 0))
        visited = set()
        visited.add(target.val)
        
        while q:
            
            curr_node, level = q.popleft()
            
            if level > K:
                return ans
            
            if level == K:
                
                ans.append(curr_node)
            
            
            for child in graph[curr_node]:
                
                if child not in visited:
                    visited.add(child)
                    q.append((child, level+1))
        
        
        return ans
                
            
            
            
            
            