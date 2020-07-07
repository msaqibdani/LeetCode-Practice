# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        fast = slow = head
        
        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next
            
            #cycle found
            if slow == fast:
                break
        
        #if no cycle found
        else:
            return None
        
        
        temp = head
        while temp != slow:
            slow = slow.next
            temp = temp.next
        
        
        return temp
        