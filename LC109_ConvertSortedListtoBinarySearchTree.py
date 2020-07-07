# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        
        arr = []
        temp = head
        
        while temp:
            arr.append(temp.val)
            temp = temp.next
        
        
        prev = ListNode('inf')
        
        def helper(left, right):
            nonlocal arr
            
            if left > right:
                return None
            
            
            mid = (left+right)//2
            
            node = TreeNode(arr[mid])
            
            if left == right:
                return node
            
            node.left = helper(left, mid-1)
            node.right = helper(mid+1, right)
            
            return node
        
        
        prev.next = helper(0, len(arr)-1)
        return prev.next
            
            
            
        