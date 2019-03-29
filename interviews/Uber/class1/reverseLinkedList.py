"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
        
    def reverse(self, head):
        # write your code here
        
        prev = None 
        
        curr = head 
        
        while curr is not None:
            
            next_node = curr.next 
            
            curr.next = prev 
            
            prev = curr 
            
            curr = next_node
            
        return prev