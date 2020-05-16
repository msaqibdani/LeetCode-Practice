# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    
    '''
    n = 2
    p = prev, s = start, e = end
    
    1->2->3->4->5
          p  s  e
    
      
    '''
    
    if not head or not n:
        return head
    
    if not head.next and n == 1:
        return None
    
    prev = None
    difference = 1
    start = end = head
    
    #creating a window
    while difference < n:
        end = end.next
        difference += 1
    
    #moving window to the end
    while end and end.next:
        prev = start
        start = start.next
        end = end.next
    
    #if first element needs to be removed
    if not prev:
        head = head.next
        return head
    
    prev.next = start.next
    
    return head
    
    
    