"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: a ListNode
    @return: a ListNode
    """
    def swapPairs(self, head):
        # write your code here
        
        if head is None or head.next is None:
            
            return head 
        
        dummy = ListNode(0, head)
        
        prev = dummy 
        
        while head and head.next:
            
            succ = head.next 
            temp = succ.next 
            
            prev.next = succ 
            succ.next = head 
            head.next = temp 
            
            prev = head  
            head = temp
            
        return dummy.next 