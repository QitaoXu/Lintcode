"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        
        l = ListNode(-1)
        
        head = l
        
        while l1 is not None and l2 is not None:
            
            if l1.val < l2.val:
                
                l.next = ListNode(l1.val)
                
                l = l.next
                l1 = l1.next
                
            else:
                
                l.next = ListNode(l2.val)
                
                l = l.next
                l2 = l2.next
                
        while l1 is not None:
            
            l.next = ListNode(l1.val)
            
            l = l.next 
            
            l1 = l1.next 
            
            
        while l2 is not None:
            
            l.next = ListNode(l2.val)
            
            l = l.next
            
            l2 = l2.next 
            
        return head.next 