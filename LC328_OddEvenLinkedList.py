# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def oddEvenList(self, head: ListNode) -> ListNode:
    
    #less than two nodes
    if not head or not head.next:
        return head
    
    odd, even = head, head.next
    even_start = head.next
    
    #2 or more than 2 nodes
    while even and even.next:
        
        odd.next = even.next
        odd = odd.next
        
        even.next = odd.next
        even = odd.next
        
        
        
    odd.next = even_start
    
    
    return head
        
    
        
        
        
        
        
        
      
                
        
        
        
        
        